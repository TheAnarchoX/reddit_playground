# -*- coding: utf-8 -*-

"""Console script for python_playground."""
import sys
import click
import configparser
import os
from python_playground.lib.GlobalContext import GlobalContext
@click.command()
@click.option("-v", "--verbose", is_flag=True, help='run Python Playground in verbose mode')
def main(verbose):

    os.environ["PLAYGROUND_VERBOSE"] = str(verbose).upper()


    config = configparser.ConfigParser()
    config.read('./config/config.ini')
    if os.getenv("PLAYGROUND_VERBOSE") == "TRUE":
        print(f"Starting Python Playground (v{config.get('PLAYGROUND', 'VERSION')})")

    # Initialize the GlobalContext
    context = GlobalContext()


    return 0

if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
