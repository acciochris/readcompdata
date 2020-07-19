"""Main entry point for Readcomp-data"""

import sys
import argparse
import importlib
import os


def main(args=None):
    if not args:
        args = sys.argv[1:]
    parser = argparse.ArgumentParser(
        prog="python -m readcompdata", description="Utility to get data for Readcomp."
    )
    parser.add_argument(
        "-s", "--server", nargs="+", help="server(s) to get data from", required=True
    )
    parser.add_argument("-o", dest="output", help="output directory", default="data")
    opts = parser.parse_args(args)
    try:
        os.mkdir(opts.output)
    except FileExistsError:
        pass
    for server in opts.server:
        server = __import__(server, level=1, globals=globals())
        texts = server.get()
        for i, text in enumerate(texts):
            with open(os.path.join(opts.output, "{}.txt".format(i)), "w") as f:
                f.write(text)


main()
