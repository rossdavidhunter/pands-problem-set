# use of import for date and time

from datetime import datetime

today = datetime.today()

Final = today.strftime("%A, %d %b %Y at %H:%M%p")
print(Final)



