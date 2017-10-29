import json

class MultipleRequestsController(object):

    def __init__(self, config):
        try:
            with open(config) as json_data:
                self.config = json.load(json_data)
        except:
            self.config = None

    def __str__(self):
        if(self.config):
            if(len(self.config) > 0):
                ret = ""
                for request in self.config:
                    ret += "Url: " + request['url'] + " Method: " + request['method'] + "\n"
                return ret
            else:
                return "Empty configuration file."
        else:
            return "Configuration file not found."
