import os
import sys
import string
import json
import webapp2

__author__ = 'TZ Martin (@tzmartin)'
__website__ = 'www.tzmartin.com'

class App(webapp2.RequestHandler):
    def get(self):

        #self.send_response(200)
        self.response.headers['Content-Type'] = 'application/json'
        
        file_arg = "source.json"

        try:
            content = json.loads(open(file_arg).read())
            
            path = self.request.path[1:]

            components = string.split(path, '/')
            print components

            node = content
            for component in components:
                if len(component) == 0 or component == "favicon.ico":
                    continue

                if type(node) == dict:
                    node = node[component]

                elif type(node) == list:
                    node = node[int(component)]
                    
        except IOError:
            self.response.set_status(404)
            node = json.loads("{\"error\":\"Couldn't find source\"}")
            

        self.response.write(json.dumps(node,sort_keys=True, indent=4, separators=(',', ': ')))
        
        return

app = webapp2.WSGIApplication([
    (r'/.*', App)],
debug=os.environ['SERVER_SOFTWARE'].startswith('Dev'))
