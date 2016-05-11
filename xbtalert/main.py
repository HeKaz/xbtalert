import argparse
import sys
import json

from utils import get_version


parser = argparse.ArgumentParser()

parser.add_argument('-c', '--config',
                    action='store',
                    help='specify configuration file',
                    default="../config.json",
                    dest='configfile')

parser.add_argument('-f', '--foreground',
                    action='store_true',
                    help='run in foreground',
                    default=False,
                    dest='foreground'
                    )

parser.add_argument('-p', '--pidfile',
                    action='store',
                    help='specify pid file',
                    default=None,
                    dest='pidfile')

parser.add_argument('-v', '--version',
                    action='store_true',
                    help='display the version and exit',
                    default=False,
                    dest='version')

args = parser.parse_args()

if args.version:
    print("XBTAlert version " + get_version())
    sys.exit(0)


