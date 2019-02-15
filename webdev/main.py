#!/usr/bin/env python

import webapp2

# Implementing HTML escaping to control userinput

form = """
<form method="post">
    What is your birthday?
    <br>
    <label> Month <input type=""text" name="month" value="%(month)s"> </label>
    <label> Day <input type=""text" name="day" value="%(day)s"> </label>
    <label> Year <input type=""text" name="year" value="%(year)s"> </label>
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

#Escaping the HTML using cgi function and line#67
import cgi
def escape_html(s):
    return cgi.escape(s, quote = True)

class MainPage(webapp2.RequestHandler):
    def write_form(self, error="", month="", day="", year=""):       # Adding other userinput parameters
        self.response.out.write(form % {"error" : error, "month" : escape_html(month), "day" : escape_html(day), "year" : escape_html(year)})

    def get(self):
    	self.write_form()           # Using the write form function from the above
    
    def post(self):             # Adding the post function here since we changed the method to post
    	user_month = self.request.get('month')
        user_day = self.request.get('day')
        user_year = self.request.get('year')

        month = valid_month(user_month)
        day = valid_day(user_day)
        year = valid_year(user_year)

        if not (month and day and year): # If the input voilates any of the above three functions (validation logic), the user will be re-presented the form through below line:
            self.write_form("That doesn't look valid to me, friend.", user_month, user_day, user_year) # Passing userinputs to preserve what the user has typed in, in case the input fails validation
        else:
            self.response.out.write("Thanks! That's a totally valid day!")  # Say thanks to the user

app = webapp2.WSGIApplication([('/', MainPage)], debug=True)

