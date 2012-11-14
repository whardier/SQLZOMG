#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import sys
import argparse
import logging
import urlparse

import sqlzomg

################################################################################
## ┏┳┓┏━┓╻┏┓╻
## ┃┃┃┣━┫┃┃┗┫
## ╹ ╹╹ ╹╹╹ ╹

def main():
    epilog = """DATABASEURI examples:

  For PostgreSQL (Requires psychopg2):
    postgresql://[user[:password]@][netloc][:port]/dbname

  For SQLlite3+Spatialite (Requires pyspatialite):
    file:data.db
    file:/home/fred/data.db
    file:///home/fred/data.db    
"""

    epilog_general = epilog + """

You should initialize the database by running:

  sqlzomg DATABASEURI init
"""
    
    parser = argparse.ArgumentParser(description=sqlzomg.__description__, formatter_class=argparse.RawTextHelpFormatter, epilog=epilog_general)

    parser.add_argument('database',
        action='store',
        help='''ex: postgresql://[user[:password]@][netloc][:port]/dbname
ex: file:data.db''',
        metavar='DATABASEURI')

    parser.add_argument('-v',
        dest='verbose',
        action='count',
        help='add multiple times for increased verbosity')

    subparsers = parser.add_subparsers(title='Command', dest='command')

    init_parser = subparsers.add_parser('init', help='Initialize the database',  formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)

    init_parser.add_argument('--erase',
        action='store_false',
        help='erase existing database')

    play_parser = subparsers.add_parser('play', help='Start up a game',  formatter_class=argparse.RawDescriptionHelpFormatter, epilog=epilog)

    play_parser.add_argument('username',
        action='store',
        metavar='USERNAME')

    args = parser.parse_args()

    loglevel = logging.CRITICAL

    if args.verbose >= 4:
        loglevel = logging.DEBUG
    elif args.verbose == 3:
        loglevel = logging.INFO
    elif args.verbose == 2:
        loglevel = logging.WARNING
    elif args.verbose == 1:
        loglevel = logging.ERROR

    logging.basicConfig(level=loglevel)

    logger = logging.getLogger('Arguments')

    for arg, value in vars(args).iteritems():
        logger.debug('%s:%s' % (arg, value))

    logger = logging.getLogger('General')
    logger.info('ZOMGing')

    return

if __name__ == '__main__':
    sys.exit(main())
