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
    	q = self.request.get("q") # This will grab the query "q" parameter from request.get and store it in variable "q"
        self.response.out.write(q) # Printing the "q" from above this time instead of form which was printed earlier. 

app = webapp2.WSGIApplication([('/', MainPage),('/testform', TestHandler)], debug=True)
