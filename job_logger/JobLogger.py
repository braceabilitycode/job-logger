import requests
import json
import datetime
from configparser import ConfigParser
import uuid
import os

class Job_Logger:

    url=''
    guid=''
    job_name=''
    headers = { 'Accept' : 'application/json', 'Content-Type' : 'application/json'}

    def __init__(self):
        print(f'Working directory is: {os.getcwd()}')
        config = ConfigParser()
        config_file ='./config.ini'
        config.read(config_file)

        self.url = config['job_logger']['url']

    def Start(self,the_job_name):
        self.job_name=the_job_name
        self.guid = str(uuid.uuid4())
        data={
                "TraceId":self.guid,
                "Type":"Started",
                "JobName":self.job_name,
                "CreatedAt":str(datetime.datetime.now())
            }

        requests.post(self.url, data=json.dumps(data), headers=self.headers)

    def Stop(self):
        data={
                "TraceId":self.guid,
                "Type":"Completed",
                "JobName":self.job_name,
                "CreatedAt":str(datetime.datetime.now())
            }
    
        requests.post(self.url, data=json.dumps(data), headers=self.headers)

    def Exception(self,exception):
        data={
                "TraceId":self.guid,
                "Type":"Exception",
                "JobName":self.job_name,
                "CreatedAt":str(datetime.datetime.now()),
                "Error":str(exception)
            }
    
        requests.post(self.url, data=json.dumps(data), headers=self.headers)
    
    def Warning(self,Warning):
        data={
                "TraceId":self.guid,
                "Type":"Warning",
                "JobName":self.job_name,
                "CreatedAt":str(datetime.datetime.now()),
                "Warning":str(Warning)
            }
    
        requests.post(self.url, data=json.dumps(data), headers=self.headers)

