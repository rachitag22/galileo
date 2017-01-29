import requests
import json

string = "arr = ["
request = requests.get("http://api.umd.io/v0/map/buildings")
parsedJson = request.json()
for buildingInfo in parsedJson:
    string += buildingInfo["name"] + ", "
print string