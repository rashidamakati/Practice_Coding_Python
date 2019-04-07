import requests
import json
from math import sin, cos, sqrt, atan2, radians
import time

json_data = json.loads(requests.get("https://app.scoot.co/api/v1/scooters.json").text)

latinput = input("Enter Latitude: ")
longinput = input("Enter Longitude: ")

#Function to loop through every Latitude and Longitude of given vehicle in the JSON file and calculating the distance with the Coordinates of the Input.
def jsonfileloop(print_result):
    final_vehicals = []
    for i in range(len(json_data["scooters"])-1):
        checkdist = getCoordinates(latinput,longinput, json_data["scooters"][i]["latitude"], json_data["scooters"][i]["longitude"])
        if checkdist <= 300:
            final_vehicals.append(json_data["scooters"][i]["id"])
    return final_vehicals


#Function to calculate the distance between two coordinates and return the value in meters
def getCoordinates(lat1, long1 ,scootlat1, scootlong1):

    earthradius = 6373000.0
    lat = radians(float(lat1))
    long = radians(float(long1))
    scootlat = radians(float(scootlat1))
    scootlong = radians(float(scootlong1))

    distlong = scootlong - long
    distlat = scootlat - lat

    calcdist = sin(distlat/2)**2+cos(lat)*cos(scootlat)*sin(distlong/2)**2
    distcor = 2 * atan2(sqrt(calcdist), sqrt(1-calcdist))
    distance = earthradius * distcor

    return distance


while(True):

    #Getting the final list of vehicles that are within the distance of 300 meters for the given coordinates
    scoots_in_dist = jsonfileloop(json_data)
    print(scoots_in_dist)

    #Calling the function every 5 seconds
    time.sleep(5)





# # Associate Software Engineer Programming Challenge:
# #
# # Build a program that takes a coordinate (latitude and longitude - a location somewhere in San Francisco) as input, and displays a list of vehicles that are within 300 meters of that location. This list should stay up to date and accurate as often as every few seconds.
# #
# # You can code in any language that you are most proficient in.
# #
# # You can retrieve the list of vehicles from this API
# # https://app.scoot.co/api/v1/scooters.json
#
