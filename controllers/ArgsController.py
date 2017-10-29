import argparse, sys
from controllers.SingleRequestController import SingleRequestController
from controllers.MultipleRequestsController import MultipleRequestsController
from models.Version import Version

class ArgsController(object):

    def getParsedArgs(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('-v', '--version', dest='version', action='store_true', help="show program version and exit")
        parser.add_argument('-c', '--config', help="configuration file in JSON format")
        parser.add_argument('-u', '--url', help="complete url")
        parser.add_argument('-m', '--method', help="HTTP method")
        return parser.parse_args()

    def __init__(self):
        args = self.getParsedArgs()
        if(args.version):
            print(Version())
            sys.exit()
        elif(args.config and (len(sys.argv) == 3)):
            print(MultipleRequestsController(args.config))
        elif(args.url and args.method and (len(sys.argv) == 5)):
            print(SingleRequestController(args.url, args.method))
        else:
            print("Invalid command, check help with -h or --help for more information")
            sys.exit()
