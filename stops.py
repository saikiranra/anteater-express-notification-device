import math

class Stops:
    def __init__(self , name , lat , lon):
        self.name = name
        self.lat = lat
        self.lon = lon

    def get_coordinates(self):
        return((self.lat , self.lon))

    def in_radius(self , vehicle , rad = 0.00757576):
        #print(self.get_coordinates())
        #print(vehicle.get_coordinates())
        latD = math.radians(self.lat - vehicle.lat)
        lonD = math.radians(self.lon - vehicle.lon)
        a = (math.sin(latD/2)**2) + (math.cos(math.radians(vehicle.lat)) * math.cos(math.radians(self.lat)) * (math.sin(lonD/2)**2))
        c = 2 * math.atan2(math.sqrt(a) , math.sqrt(1-a))
        r = c * 3961
        #print("{} {}".format(vehicle.name , r))
        return r <= rad
