import boto3
import logging
from botocore.exceptions import ClientError
import datecompare
import datetime
import config



class Accesskey():
    #构造函数
    def __init__(self,Region_name:str)->None:
        self.client = boto3.client('iam',region_name = Region_name)
    
    #查询accesskey,输出一个嵌套字典
    def view_access_key(self,user_name:str)->dict: 
        try:
            keys = self.client.list_access_keys(
                UserName = user_name,
            )
            return keys
        except ClientError as e:
            logging.error(e)
            
        
    #以列表形式输出指定用户的accesskey
    def get_key_list(self,username:str)->dict:
        res = Accesskey.view_access_key(self,username)
        Metadata:list = res['AccessKeyMetadata']
        list = []
        for i in Metadata:
            id = i['AccessKeyId']
            list.append(id)
        return list        
        
    #创建accesskey
    def create_access_key(self,username:str)->None:
        try:
            res:dict = self.client.create_access_key(
                UserName = username  #指定所新建的accesskey的归属用户
            )
            print(res['AccessKey'])
        except ClientError as e :
            logging.error(e)

    #删除指定的accesskey
    def delete_access_key(self,username:str,access_key:str)->None:
        try:
            self.client.delete_access_key(
                AccessKeyId = access_key,
                UserName = username
            )
        except ClientError as e:
            logging.error(e)
    

    #计算key的生命周期,如果周期超过life参数，则进行一定的操作
    def deal_with_key(self,username:str,life:int)->None:
        keys = self.client.list_access_keys(
            UserName = username,
        )
        dict = keys['AccessKeyMetadata']
        for i in dict:
            logging.info('UserName =',i['UserName'],'AccessKeyId =',i['AccessKeyId'],'CreateDate =',i['CreateDate'])
            #将accesskey的CreateDate由datetime类型转换为string
            #i['CreateDate']是datetime.datetime类型
            key_time:str = i['CreateDate'].strftime('%Y-%m-%d %H:%M:%S') #把类型从datetime转为string类型
            logging.info('This key is created at: {}'.format(key_time))
            now_Time = datecompare.get_time()
            diff:int = datecompare.date_compare(now_Time,key_time) #计算key的创建日期和当前系统时间的天数差值
            logging.info('Key life is:',diff,'days')
            #业务逻辑
            if diff >= life:
                print('Update this Key')
                Accesskey.Inactive_key_status(self,username,i['AccessKeyId'])
            else:
                print('No action is needed')
            
    #更新key的状态为Inactive
    def inactive_key_status(self,username,access_key)->None:
        self.client.update_access_key(
            UserName = username,
            AccessKeyId = access_key,
            Status = 'Inactive'
        )
        logging.info('The key {}'.format(access_key),'is Active')

    #更新key的状态为Active
    def active_key_status(self,username,access_key)->None:
        self.client.update_access_key(
            UserName = username,
            AccessKeyId = access_key,
            Status = 'Active'
        )
        logging.info('The key {}'.format(access_key),'is Inactive')

    #根据所给的key，计算该key的目前寿命并返回
    def get_key_life(self,username:str,access_key:str)->int:
        keys = self.client.list_access_keys(
            UserName = username,
        )
        dict = keys['AccessKeyMetadata']
        try:
            for i in dict:
                if i['AccessKeyId'] == access_key:
                    key_time:str = i['CreateDate'].strftime('%Y-%m-%d %H:%M:%S')
                    now_Time = datecompare.get_time()
                    diff:int = datecompare.date_compare(now_Time,key_time)
                    logging.info('The keys life is : {}'.format(diff))
                    return diff
        except ClientError as e:
            logging.error(e)
    
    #当前这个key已经超时，需要删除此key再重新生成一个key
    def generate_access_key(self,username:str,access_key:str)->None:
        Accesskey.delete_access_key(self,username,access_key)
        Accesskey.create_access_key(self,username)
        logging.info('A new key has been created for User {}'.format(username))

    #对key进行更新
    def rotation_access_key(self,username:str,life:int)->None:
        li = Accesskey.get_key_list(self,username)
        for i in li:
            ans:int = Accesskey.get_key_life(self,username,i)
            if ans >= life:
                Accesskey.generate_access_key(self,username,i)
        
        

        
        
        
        


    


    