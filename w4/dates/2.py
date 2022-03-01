import datetime
date=datetime.date.today()
delta=datetime.timedelta(1)
print("yesterday was ",date-delta)
print("today is ",date)
print("tomorrow will be ",date+delta)
