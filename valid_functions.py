
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
          
       


