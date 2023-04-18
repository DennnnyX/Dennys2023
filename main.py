import accesskey
import datecompare
import config
import logging

#config模块配置信息
conf = config.Config()
Region_name = conf.Region_name
Key_Life = conf.KEY_LIFE
USER_NAME = conf.USER_NAME


logging.getLogger().setLevel(logging.INFO)



#当前系统时间
now_Time =  datecompare.get_time()
logging.info('System time now is:{}'.format(now_Time))


#新建实例
acc = accesskey.Accesskey(Region_name)



def run():
    print('hello python')
    acc = accesskey.Accesskey(Region_name)
    list = acc.get_key_list(USER_NAME)
    print(list)

if __name__ == '__main__':
    run()








