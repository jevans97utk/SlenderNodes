# Tested on dataone.libclient version 2.0.0

import datetime
import StringIO
import requests

# D1.
import d1_common.types.dataoneTypes_v2_0 as v2
import d1_common.const
import d1_client.mnclient_2_0
import d1_common.checksum


# To generate arbitrary version PIDs, the native identifier is concatenated with datetime information.
def _generate_version_pid(native_identifier):
    return native_identifier + datetime.datetime.now().strftime("%Y-%m-%d_%H-%M")


def _generate_system_metadata(scimeta_bytes, native_identifier_sid, version_pid, symeta_settings_dict):
    sys_meta = v2.systemMetadata()
    sys_meta.seriesId = native_identifier_sid
    sys_meta.identifier = version_pid
    sys_meta.formatId = symeta_settings_dict['formatId']
    sys_meta.size = len(scimeta_bytes)
    sys_meta.checksum = \
        d1_common.checksum.create_checksum_object_from_stream(StringIO.StringIO(scimeta_bytes), algorithm='MD5')
    sys_meta.checksum.algorithm = 'MD5'
    sys_meta.dateUploaded = datetime.datetime.now()
    sys_meta.dateSysMetadataModified = datetime.datetime.now()
    sys_meta.rightsHolder = symeta_settings_dict['rightsholder']
    sys_meta.submitter = symeta_settings_dict['submitter']
    sys_meta.authoritativeMemberNode = symeta_settings_dict['authoritativeMN']
    sys_meta.originMemberNode = symeta_settings_dict['originMN']
    sys_meta.accessPolicy = _generate_public_access_policy()
    return sys_meta


def _generate_public_access_policy():
    accessPolicy = v2.AccessPolicy()
    accessRule = v2.AccessRule()
    accessRule.subject.append(d1_common.const.SUBJECT_PUBLIC)
    permission = v2.Permission('read')
    accessRule.permission.append(permission)
    accessPolicy.append(accessRule)
    return accessPolicy

# A generic client manager for use with a DataONE adapter implementation.
class D1ClientManager:

    # Initialize the client manager with an instance of a member node client
    def __init__(self, gmn_baseurl, auth_cert, auth_cert_key, sysmeta_settings_dict):
        self.client = d1_client.mnclient_2_0.MemberNodeClient_2_0(
            gmn_baseurl,
            cert_path=auth_cert,
            key_path=auth_cert_key)
        self.sysmeta_settings_dict = sysmeta_settings_dict

    # since getSystemMetadata accepts series_ID (which we populate with native identifier) as an argument, it can be
    # used to verify if a version of this record already exists in GMN.
    def check_if_identifier_exists(self, native_identifier_sid):
        try:
            self.client.getSystemMetadata(native_identifier_sid)
        except d1_common.types.exceptions.NotFound:
            return False
        else:
            return True

    def ingest_science_metadata(self, sci_metadata_bytes, native_identifier_sid):
        version_pid = _generate_version_pid(native_identifier_sid)
        system_metadata= _generate_system_metadata(sci_metadata_bytes, native_identifier_sid,
                                  version_pid, self.sysmeta_settings_dict)
        self.client.create(version_pid, StringIO.StringIO(sci_metadata_bytes), system_metadata)


    def update_science_metadata(self, sci_metadata_bytes, native_identifier_sid):
        new_version_pid = _generate_version_pid(native_identifier_sid)
        old_version_system_metadata = self.client.getSystemMetadata(native_identifier_sid)
        old_version_pid = old_version_system_metadata.identifier.value()
        new_version_system_metadata = _generate_system_metadata(sci_metadata_bytes, native_identifier_sid,
                                  new_version_pid, self.sysmeta_settings_dict)
        self.client.update(old_version_pid,
                           StringIO.StringIO(sci_metadata_bytes),
                           new_version_pid,
                           new_version_system_metadata)

