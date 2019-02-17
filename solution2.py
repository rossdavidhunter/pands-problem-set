# solution to problem 2
# to add in days of week need datetime config
from datetime import date

# create variable with days of week
Days = ('Mon','Tue','Wed','Thurs','Fri','Sat','Sun')

if (Days[date.weekday(date.today())].startswith('T')):
    print('Today begins with T')
else:
    print('Today does not begin with T')
  