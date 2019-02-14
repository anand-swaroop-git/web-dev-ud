#!/usr/bin/env python
# https://webapp2.readthedocs.io/en/latest/

import webapp2

# Adding another handler named "/testform" so that we can pass the query parameter to "/testform"
form = """
<form action="/testform">
<input name="q">
<input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
    	self.response.out.write(form) # Printing the form this time instead of "Hello World"

class TestHandler(webapp2.RequestHandler): #New Handler
    def get(self):
    	self.response.headers['Content-Type'] = 'text/plain' # So that browser doesn't render the server response
        self.response.out.write(self.request) # This time, we want to print the complete GET request which will show us ==> GET /testform?q=whatever as the first line 

app = webapp2.WSGIApplication([('/', MainPage),('/testform', TestHandler)], debug=True)

# Output of the above program is below:
# GET /testform?q=whatever HTTP/1.1
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
# Accept-Language: en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6
# Host: localhost:10080
# Referer: http://localhost:10080/
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
# X-Appengine-Country: ZZ