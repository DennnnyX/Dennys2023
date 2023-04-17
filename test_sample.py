import logging
import datetime
import time

def date_compare(date1:str,date2:str)->int:
    try:
        time1 = time.mktime(time.strptime(date1, '%Y-%m-%d %H:%M:%S'))
        time2 = time.mktime(time.strptime(date2, '%Y-%m-%d %H:%M:%S'))
        diff = int(time1) - int(time2) #转化为Int类型
        return int(diff / 24 / 60 / 60)
    except:
        logging.error("date2 is ahead of date1")

class Test_auto:
    def test_date_compare():
        assert date_compare('2023-04-14','2023-04-14') == 0