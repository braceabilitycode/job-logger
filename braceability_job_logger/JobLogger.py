import requests
import json
import datetime
from configparser import ConfigParser
import uuid

class Job_Logger:

    url=''
    guid=''
    job_name=''
    headers = { 'Accept' : 'application/json', 'Content-Type' : 'application/json'}

    def __init__(self):
        config = ConfigParser()
        config_file ='./config.ini'
        config.read(config_file)

        self.url = config['job_logger']['url']
        self.guid = str(uuid.uuid4())

    def StartJob(self,the_job_name):
        self.job_name=the_job_name
        data={
                "TraceId":self.guid,
                "Type":"Started",
                "JobName":self.job_name,
                "StartedAt":str(datetime.datetime.now())
            }

        requests.post(self.url, data=json.dumps(data), headers=self.headers)

    def StopJob(self):
        data={
                "TraceId":self.guid,
                "Type":"Completed",
                "JobName":self.job_name,
                "CompletedAt":str(datetime.datetime.now())
            }
    
        requests.post(self.url, data=json.dumps(data), headers=self.headers)
    

