import time
import datetime
import logging


#date1是当前系统时间，date2是accesskey生成时间
def date_compare(date1:str,date2:str)->int:
    try:
        time1 = time.mktime(time.strptime(date1, '%Y-%m-%d %H:%M:%S'))
        time2 = time.mktime(time.strptime(date2, '%Y-%m-%d %H:%M:%S'))
        diff = int(time1) - int(time2) #转化为Int类型
        return int(diff / 24 / 60 / 60) #从秒数差距转化为天数差距
    except:
        logging.error("date2 is ahead of date1")
        exit(1) #发生错误，异常退出
    

