import runpy
import time




while 1:
    cur_time = time.ctime()
    day, month, date, times, year = cur_time.split(" ")
    # abs_time1, abs_time2 = times.spilt(":")
    # print(abs_time1)
    # print(abs_time2)
    time1, time2, time3 = times.split(":")
    print(time1)
    print(time2)
    # if cur_time == "19:03:00":
    #     runpy.run_path(path_name='test.py')