import argparse, sys
from version import Version

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-v', '--version', dest='version', action='store_true', help="show program version and exit")
    parser.add_argument('-c', '--config', help="configuration file")
    args = parser.parse_args()

    if(args.version):
        print(Version())
        sys.exit()

    if(args.config):
        print("Config " + str(args.config))
