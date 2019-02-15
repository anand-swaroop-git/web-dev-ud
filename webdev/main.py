#!/usr/bin/env python

import webapp2

# Removed the action of submitting the query parameter to the TestHandler, the TestHandler definition itself as well as the URL mapping in the last line
# Also added three input boxes to enter the DOB
# At this point, the webapp will accept whatever parameter user has passed in and will greet the user with a "Thanks" message.

form = """
<form method="post">
    What is your birthday?
    <br>
    <label>Month<input type="text" name="month"></label>
    <label>Day<input type="text" name="day"></label>
    <label>Year<input type="text" name="year"></label>
    <br>
    <br>
<input type="submit">
</form>
"""

class MainPage(webapp2.RequestHandler):
    def get(self):
    	self.response.out.write(form)           # Printing the form
    
    def post(self):             # Adding the post function here since we changed the method to post
    	self.response.out.write("Thanks! That's a totally valid day!") 

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)

