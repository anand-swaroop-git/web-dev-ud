#!/usr/bin/env python

import webapp2

# Removed the action of submitting the query parameter to the TestHandler, the TestHandler definition itself as well as the URL mapping in the last line
# Also added three input boxes to enter the DOB
# At this point, if the user enters a valid DOB, he will be greeted with "Thanks" and if he enters incorrect entries, he will be re-presented the form.

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

# This is the validation logic where we are validating the user input
# Now we need to valid month function a bit more userfriendly therefore, we have added a logic that if a user types in the first three characters of any month, the function will return that month in the output

months = ['January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July',
          'August',
          'September',
          'October',
          'November',
          'December']

# Making a dictionary of first three characters of Month to complete month name
month_abbvs = dict((m[:3].lower(),m) for m in months)
          
def valid_month(month):
  if month:
    short_month = month[:3].lower()
    return month_abbvs.get(short_month)


# Valid Day Function
def valid_day(day):
  if day and day.isdigit():
    day = int(day)
    if day > 0 and day <= 31:
      return day
      
# Valid Year Function      
def valid_year(year):
  if year and year.isdigit():
    year = int(year)
    if year > 1900 and year < 2020:
      return year


class MainPage(webapp2.RequestHandler):
    def get(self):
    	self.response.out.write(form)           # Printing the form
    
    def post(self):             # Adding the post function here since we changed the method to post
    	user_month = valid_month(self.request.get('month'))         # Adding the validation logic
    	user_day = valid_day(self.request.get('day'))       # Adding the validation logic
    	user_year = valid_year(self.request.get('year'))        # Adding the validation logic

        if not (user_month and user_day and user_year): # If the input voilates any of the above three functions (validation logic), the user will be re-presented the form through below line:
            self.response.out.write(form)
        else:
            self.response.out.write("Thanks! That's a totally valid day!")  # Say thanks to the user

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)

