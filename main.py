import stops
import vehicle
import default_device

import time
import json
import math
try:
    #Python 2
    import urllib2 as ul
    from StringIO import StringIO
except:
    #Python 3
    import urllib.request as ul
    from io import StringIO


WEB_SITE = "https://www.ucishuttles.com/Route/{}/Vehicles"
ROUTE_ID = 530

def get_response(url):
    #Returns text from url request
    resp = ul.urlopen(url)
    respText = resp.read()
    resp.close()
    return respText.decode("utf-8") 

def string_to_json(text):
    return json.load(StringIO(text))


def main():
    #Create list of stops
    stop_list = []
    stop_list.append(stops.Stops("VDC Stop 1" , 33.640899 , -117.823073))
    stop_list.append(stops.Stops("VDC Stop 2" , 33.639276, -117.824100))
    stop_list.append(stops.Stops("VDC Stop 3" , 33.638173, -117.825505))

    def_dev = default_device.default_device("Shell")
    def_dev.connect()
    while(1):
        #Get json text
        json_text = get_response(WEB_SITE.format(ROUTE_ID))
        #text to json obj
        json_obj = string_to_json(json_text)
        #Create list of vehicles
        vehicle_list = []
        for v in json_obj:
            vehicle_list.append(vehicle.Vehicle(v))
        
        
        for v in vehicle_list:
            for s in stop_list:
                if(s.in_radius(v)):
                    def_dev.action(s , v)
            
        time.sleep(10)

    def_dev.disconnect()

if __name__ == "__main__":
    main()
