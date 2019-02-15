#!/usr/bin/env python

import webapp2

# Adding string substitution logic @line#14, writing a function to utilize string substitution @line#62

form = """
<form method="post">
    What is your birthday?
    <br>
    <label>Month<input type="text" name="month"></label>
    <label>Day<input type="text" name="day"></label>
    <label>Year<input type="text" name="year"></label>
    <div style="color: red">%(error)s</div>
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
    def write_form(self, error=""):       # Creating the write form function so that we could pass on the error as string substitution
        self.response.out.write(form % {"error": error})

    def get(self):
    	self.write_form()           # Using the write form function from the above
    
    def post(self):             # Adding the post function here since we changed the method to post
    	user_month = valid_month(self.request.get('month'))         # Adding the validation logic
    	user_day = valid_day(self.request.get('day'))       # Adding the validation logic
    	user_year = valid_year(self.request.get('year'))        # Adding the validation logic

        if not (user_month and user_day and user_year): # If the input voilates any of the above three functions (validation logic), the user will be re-presented the form through below line:
            self.write_form("That doesn't look valid to me, friend.")
        else:
            self.response.out.write("Thanks! That's a totally valid day!")  # Say thanks to the user

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)

