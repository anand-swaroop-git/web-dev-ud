#!/usr/bin/env python
# https://webapp2.readthedocs.io/en/latest/

import webapp2

# Adding the simple search engine logic with the help of a form
form = """
<form action="http://www.google.com/search">
<input name="q">
<input type="submit">
</form>
"""



class MainPage(webapp2.RequestHandler):
    def get(self):
    	self.response.headers['Content-Type'] = 'text/html' # So that the browser can render the HTML
        self.response.write(form) # Printing the form this time instead of "Hello World"

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
