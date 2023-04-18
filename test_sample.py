import logging
import datetime
import time
import pytest

def date_compare(date1:str,date2:str)->int:
    try:
        time1 = time.mktime(time.strptime(date1, '%Y-%m-%d %H:%M:%S'))
        time2 = time.mktime(time.strptime(date2, '%Y-%m-%d %H:%M:%S'))
        diff = int(time1) - int(time2) #转化为Int类型，结果为秒数
        return int(diff / 24 / 60 / 60) #从秒数差距转化为天数差距
    except:
        logging.error("date2 is ahead of date1")
        exit(1) #发生错误，异常退出

class Test_sample:
    def test_one(self):
        ans1 = date_compare('2023-04-17 14:11:26','2023-04-16 14:11:26')
        ans2 = date_compare('2023-04-17 14:11:26','2023-04-17 10:11:26')
        ans3 = date_compare('2023-04-17 14:11:26','2024-04-17 14:11:26')
        assert ans1 == 1
        assert ans2 == 0
        assert ans3 == -366
