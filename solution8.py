# use of import for date and time

from datetime import datetime

today = datetime.today()

Final = today.strftime("%B %d, %Y")
print(Final)



