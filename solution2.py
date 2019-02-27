# Ross Hunter, 2019 Solution 2 begins with a T

#Adapted from:https://www.pythonforbeginners.com/basics/python-datetime-time-examples

# to add in days of week need datetime config via import
import datetime as dt

# create variable with day of week using strftime and "%A"
Day = (dt.date.today().strftime("%A"))

# use of if, else and startswith
if (Day.startswith('T')):
    print('Today begins with T')
else:
    print('Today does not begin with T')

# This prints out day also on line below
print(Day)
  