from datetime import datetime

c = datetime.now()

current_time = c.strftime('%H:%M:%S')
print('Current TIme is:', current_time)
