
# A simple valid month function

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
          
def valid_month(month):
    if month.capitalize() in months:
      print (month.capitalize())
    else:
      print("Invalid month!")
          
       


