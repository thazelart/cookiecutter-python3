import argparse


def parseArguments():
    """Package argument parser."""
    parser = argparse.ArgumentParser()
    parser.add_argument("-r", "--required", required=True, help="required argument")
    parser.add_argument(
        "-o", "--optional", required=False, default="default", help="optional argument"
    )
    return parser.parse_args()
