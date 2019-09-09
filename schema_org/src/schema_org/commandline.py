# Standard library imports
import argparse
import asyncio

# 3rd party library imports
import d1_scimeta.util

# Local imports
from .arm import ARMHarvester
from .cuahsi import CUAHSIHarvester
from .ieda import IEDAHarvester
from .check_sitemap import D1CheckSitemap
from .html import D1CheckHtmlFile
from .xml_validator import XMLValidator


def setup_parser(id):

    description = f"Harvest metadata from {id.upper()}."
    epilog = (
        "Not supplying an argument to both the certificate and key arguments "
        "will disable client side authentication."
    )
    parser = argparse.ArgumentParser(
        description=description,
        epilog=epilog,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    help = f"Verbosity level of log file {id}.log"
    choices = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    parser.add_argument('-v', '--verbose', choices=choices, default='INFO',
                        help=help)

    help = (
        "Harvest records to this dataone node host.  This is NOT "
        "the host where the site map is found."
    )
    parser.add_argument('--host', default='localhost', help=help)

    help = "DataONE host SSL port."
    parser.add_argument('--port', default=443, type=int, help=help)

    help = 'Path to dataone host certificate.'
    parser.add_argument('--certificate', default=None, help=help)

    help = 'Path to dataone host private key.'
    parser.add_argument('--key', default=None, help=help)

    help = "Limit number of documents retrieved to this number."
    parser.add_argument('--num-documents', type=int, default=-1, help=help)

    help = (
        "Limit documents retrieved to those that match this regular "
        "expression."
    )
    parser.add_argument('--regex', help=help)

    help = (
        "Limit number of workers operating asynchronously to this number. "
    )
    parser.add_argument('--num-workers', type=int, default=1, help=help)

    help = (
        "Limit number of errors to this number."
    )
    parser.add_argument('--max-num-errors', type=int, default=1, help=help)

    return parser


def d1_check_html():

    description = (
        "Check a single landing page for validity.  This will validate only "
        "the JSON-LD, it will not look at the referenced XML metadata file."
    )
    parser = argparse.ArgumentParser(description=description)

    help = "path to local HTML file"
    parser.add_argument('htmlfile', type=str, help=help)

    help = f"log verbosity level"
    choices = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    parser.add_argument('-v', '--verbose', choices=choices, default='INFO',
                        help=help)

    args = parser.parse_args()

    obj = D1CheckHtmlFile(args.htmlfile, verbosity=args.verbose)
    obj.run()


def d1_check_site():

    parser = argparse.ArgumentParser()

    help = "URL of site map"
    parser.add_argument('sitemap', type=str, help=help)

    help = f"Log verbosity level"
    choices = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    parser.add_argument('-v', '--verbose', choices=choices, default='INFO',
                        help=help)

    help = "Limit number of documents retrieved to this number."
    parser.add_argument('--num-documents', type=int, default=-1, help=help)

    help = (
        "Limit number of workers operating asynchronously to this number. "
    )
    parser.add_argument('--num-workers', type=int, default=1, help=help)

    help = (
        "Limit number of errors to this number."
    )
    parser.add_argument('--max-num-errors', type=int, default=3, help=help)

    args = parser.parse_args()

    obj = D1CheckSitemap(sitemap_url=args.sitemap,
                         num_workers=args.num_workers,
                         verbosity=args.verbose,
                         num_documents=args.num_documents,
                         max_num_errors=args.max_num_errors)
    asyncio.run(obj.run())


def arm():
    parser = setup_parser("arm")
    args = parser.parse_args()

    arm_harvester = ARMHarvester(host=args.host, port=args.port,
                                 verbosity=args.verbose,
                                 certificate=args.certificate,
                                 private_key=args.key,
                                 num_documents=args.num_documents,
                                 num_workers=args.num_workers,
                                 max_num_errors=args.max_num_errors)
    asyncio.run(arm_harvester.run())


def cuahsi():
    parser = setup_parser("cuahsi")
    args = parser.parse_args()

    harvester = CUAHSIHarvester(
        host=args.host, port=args.port,
        verbosity=args.verbose,
        certificate=args.certificate,
        private_key=args.key,
        num_documents=args.num_documents,
        num_workers=args.num_workers,
        max_num_errors=args.max_num_errors,
        regex=args.regex
    )
    asyncio.run(harvester.run())


def ieda():
    parser = setup_parser("ieda")
    args = parser.parse_args()

    ieda_harvester = IEDAHarvester(host=args.host, port=args.port,
                                   verbosity=args.verbose,
                                   certificate=args.certificate,
                                   private_key=args.key,
                                   num_documents=args.num_documents,
                                   num_workers=args.num_workers,
                                   max_num_errors=args.max_num_errors)
    asyncio.run(ieda_harvester.run())


def validate():
    """
    Validate an XML document.
    """
    description = f"Validate XML metadata."
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    help = "XML file or URL"
    parser.add_argument('infile', help=help)

    help = (
        "Format ID for metadata standard.  If this argument is supplied, "
        "only that format ID will be checked.  If not, all format IDs will be "
        "checked."
    )
    parser.add_argument('--format-id',
                        help=help,
                        choices=d1_scimeta.util.get_supported_format_id_list())

    help = "Verbosity of log messages."
    choices = ['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL']
    parser.add_argument('-v', '--verbosity', help=help, choices=choices,
                        default='INFO')

    args = parser.parse_args()

    validator = XMLValidator(verbosity=args.verbosity)
    validator.validate(args.infile, format_id=args.format_id)
