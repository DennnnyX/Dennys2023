from accesskey import *
from TIME import *
import boto3
import datetime
from config import *
import logging

logging.getLogger().setLevel(logging.INFO)
logging.info('Region is : {}'.format(Region_name))
logging.info('UserName is : {}'.format(USER_NAME))
logging.info('Key_life is : {}'.format(KEY_LIFE))

#当前系统时间
now_Time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') 
logging.info('System time now is:{}'.format(now_Time))

#新建实例
acc = AK(Region_name)

#T E S T

list = acc.get_key_list(USER_NAME)
print(list)









