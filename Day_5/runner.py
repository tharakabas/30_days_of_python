import runpy
import time

while 1:
    cur_time = time.ctime()
    day, month, date, times, year = cur_time.split(" ")
    time1, time2, time3 = times.split(":")
    abs_time = time1 + time2
    if abs_time == "1923":
        runpy.run_path(path_name='test.py')
        exit(0)
