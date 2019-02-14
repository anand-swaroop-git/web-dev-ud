#!/usr/bin/env python
# https://webapp2.readthedocs.io/en/latest/

import webapp2

# Adding attribute "method" in the form to "post". By default, this method is get and this was the reason we were not required to explicitly set it to get.
form = """
<form method="post" action="/testform"> 
<input name="q">
<input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
    	self.response.out.write(form) # Printing the form this time instead of "Hello World"

class TestHandler(webapp2.RequestHandler): #New Handler
    def post(self): # Since we have changed the method in line #8 to post, we have to make the corresponding change to handler as well to avoid "method not allowed" errror. HTTP 405
    	self.response.headers['Content-Type'] = 'text/plain'    # Since we have changed the method to post, we want to see complete request. Our query parameter 'q' will come after
        self.response.out.write(self.request)                   # the HTTP request headers

app = webapp2.WSGIApplication([('/', MainPage),('/testform', TestHandler)], debug=True)

# Sample Output:
# POST /testform HTTP/1.1
# Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
# Accept-Language: en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6
# Cache-Control: max-age=0
# Content-Length: 13
# Content-Type: application/x-www-form-urlencoded
# Content_Length: 13
# Content_Type: application/x-www-form-urlencoded
# Host: localhost:10080
# Origin: http://localhost:10080
# Referer: http://localhost:10080/
# Upgrade-Insecure-Requests: 1
# User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36
# X-Appengine-Country: ZZ

# q=who+are+you
