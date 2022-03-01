import datetime
date1=datetime.datetime(2021,12,30,23,59,55,6)
date2=datetime.datetime.now()
print((date2-date1).total_seconds())