import random
from geoindex import *

#create object of class GeoGridIndex
geo_index = GeoGridIndex(precision=2)

#Populate the geo_index with Latitudes and Longitudes Information
for _ in range(10000):
    lat = random.random()*180 - 90
    lng = random.random()*360 - 180
    geo_index.add_point(GeoPoint(lat, lng))
    print(" {} {} ".geo_index.get_point_hash(GeoPoint(lat,lng)))

for _ in range(10000):
    print(" {}  {} ".format(lat,lng))

#Center Point 
center_point = GeoPoint(37.7772448, -122.3955118)


for distance, point in geo_index.get_nearest_points(center_point, 5,'km'):
    print("We found {0} in {1} km".format(point, distance))
