import time
cur_time = time.ctime()
day, month, date, times, year = cur_time.split(" ")
print(times)