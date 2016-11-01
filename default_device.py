import time

class default_device:
    def __init__(self , device_name):
        #set up device here
        self.device_name = device_name

    def connect(self):
        #init connection
        pass

    def action(self , s , v):
        #action
        print("Stop: {} Bus: {} Time: {}".format(s.name , v.name , time.ctime()))
        pass

    def disconnect(self):
        #close connection
        pass
