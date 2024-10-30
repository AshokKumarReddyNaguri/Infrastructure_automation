from datetime import datetime

c = datetime.now()

current_time = c.strftime('%H:%M:%S')
current_day = c.strftime('%A')

print('Current Date and Time: ', current_time)
print('Current Day: ', current_day)

