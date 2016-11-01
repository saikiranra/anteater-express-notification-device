class Vehicle:
    def __init__(self , dict_item):
        try:
            self.ID = dict_item["ID"]
            self.route_ID = dict_item["RouteId"]
            self.name = dict_item["Name"]
            self.lat = dict_item["Latitude"]
            self.lon = dict_item["Longitude"]
            self.updated = dict_item["Updated"]
        except:
            print("Invalid vechile object!")
            print(dict_item)
            raise

    def get_coordinates(self):
        return((self.lat , self.lon))
