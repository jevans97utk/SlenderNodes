# Standard library imports
import argparse
import asyncio

# 3rd party library imports

# Local imports
from .arm import ARMHarvester
from .ieda import IEDAHarvester
from .testtool import D1TestToolAsync, run_test_tool
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

    help = (
        'Supply a pattern to restrict records to just those that match.  This '
        'option disables the check against the last modification time in the '
        'site map.'
    )
    parser.add_argument('--regex', default=None, help=help)

    return parser


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

    args = parser.parse_args()

    obj = D1TestToolAsync(sitemap_url=args.sitemap,
                          num_workers=args.num_workers,
                          verbosity=args.verbose,
                          num_documents=args.num_documents)
    asyncio.run(run_test_tool(obj))


def arm():
    parser = setup_parser("arm")
    args = parser.parse_args()

    arm_harvester = ARMHarvester(host=args.host, port=args.port,
                                 verbosity=args.verbose,
                                 certificate=args.certificate,
                                 private_key=args.key,
                                 regex=args.regex)
    arm_harvester.run()


def ieda():
    parser = setup_parser("ieda")
    args = parser.parse_args()

    ieda_harvester = IEDAHarvester(host=args.host, port=args.port,
                                   verbosity=args.verbose,
                                   certificate=args.certificate,
                                   private_key=args.key,
                                   regex=args.regex)
    ieda_harvester.run()


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

    help = "Format ID"
    parser.add_argument('--format-id',
                        default='http://www.isotc211.org/2005/gmd',
                        help=help)

    args = parser.parse_args()

    validator = XMLValidator()
    validator.validate(args.infile, format_id=args.format_id)
