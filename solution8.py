#Ross Hunter, 2019 Solution 8 use of datetime

#Adapted from: https://www.pythonforbeginners.com/basics/python-datetime-time-examples and https://www.w3resource.com/python-exercises/python-basic-exercise-3.php

# use of import for date and time
import datetime as dt

today = dt.datetime.today()

# add date and time format to string using strftime
Final = today.strftime("%A, %d %b %Y at %H:%M%p")

print(Final)



