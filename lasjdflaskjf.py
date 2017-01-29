import requests
import json

request = requests.get("http://api.umd.io/v0/map/buildings")
parsedJson = request.json()
listOfClasses = ""

for departmentInfo in parsedJson:
    parsedJson = request.json()
    listOfClasses += departmentInfo["name"] + "\",\""
        

print listOfClasses