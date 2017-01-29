import json
import requests
import time
import cPickle as pickle

data = {'building': 'Cumberland Hall (Residence Hall)', 'day-selected': 'F', 'walking': 'false', 'classes': ["CMSC131", "ASTR101", "ENGL101S", "CPSD100", "MATH241"], 'afternoon': 'false', 'day': 'false', 'morning': 'false'}

courseDict = pickle.load(open("save.p", "rb"))

finalSchedules = []
allClasses = data["classes"]

# request = requests.get("http://api.umd.io/v0/courses/departments")
# parsedJson = request.json()
# for departmentInfo in parsedJson:
#     dept_id = departmentInfo["dept_id"]
#     request = requests.get("http://api.umd.io/v0/courses?dept_id=" + dept_id)
#     parsedJson = request.json()
#     for courseInfo in parsedJson:
#         listOfSections = courseInfo["sections"]
#         for section in listOfSections:
#             request = requests.get("http://api.umd.io/v0/courses/sections/" + section)
#             courseDict[section] = request.json()


def doesCollide(class1,class2):
    collides = False
    
    t1 = []
    t2 = []
    
    #t1
    for k in courseDict[class1]["meetings"]:
        if "M" in k["days"]:
            timePair = {"start":0,"end":0}
            timePair["start"] = (time.strptime('September 1 1969 ' + k["start_time"], '%B %d %Y %I:%M%p'))
            timePair["end"] = (time.strptime('September 1 1969 ' + k["end_time"], '%B %d %Y %I:%M%p'))
            t1.append(timePair)
                
        if "Tu" in k["days"]:
            timePair = {"start":0,"end":0}
            timePair["start"] = (time.strptime('September 2 1969 ' + k["start_time"], '%B %d %Y %I:%M%p'))
            timePair["end"] = (time.strptime('September 2 1969 ' + k["end_time"], '%B %d %Y %I:%M%p'))
            t1.append(timePair)
                
        if "W" in k["days"]:
            timePair = {"start":0,"end":0}
            timePair["start"] = (time.strptime('September 3 1969 ' + k["start_time"], '%B %d %Y %I:%M%p'))
            timePair["end"] = (time.strptime('September 3 1969 ' + k["end_time"], '%B %d %Y %I:%M%p'))
            t1.append(timePair)
                
        if "Th" in k["days"]:
            timePair = {"start":0,"end":0}
            timePair["start"] = (time.strptime('September 4 1969 ' + k["start_time"], '%B %d %Y %I:%M%p'))
            timePair["end"] = (time.strptime('September 4 1969 ' + k["end_time"], '%B %d %Y %I:%M%p'))
            t1.append(timePair)
                
        if "F" in k["days"]:
            timePair = {"start":0,"end":0}
            timePair["start"] = (time.strptime('September 5 1969 ' + k["start_time"], '%B %d %Y %I:%M%p'))
            timePair["end"] = (time.strptime('September 5 1969 ' + k["end_time"], '%B %d %Y %I:%M%p'))
            t1.append(timePair)
            
    #t2        
    for k in courseDict[class2]["meetings"]:
        if "M" in k["days"]:
            timePair = {"start":0,"end":0}
            timePair["start"] = (time.strptime('September 1 1969 ' + k["start_time"], '%B %d %Y %I:%M%p'))
            timePair["end"] = (time.strptime('September 1 1969 ' + k["end_time"], '%B %d %Y %I:%M%p'))
            t2.append(timePair)
                
        if "Tu" in k["days"]:
            timePair = {"start":0,"end":0}
            timePair["start"] = (time.strptime('September 2 1969 ' + k["start_time"], '%B %d %Y %I:%M%p'))
            timePair["end"] = (time.strptime('September 2 1969 ' + k["end_time"], '%B %d %Y %I:%M%p'))
            t2.append(timePair)
                
        if "W" in k["days"]:
            timePair = {"start":0,"end":0}
            timePair["start"] = (time.strptime('September 3 1969 ' + k["start_time"], '%B %d %Y %I:%M%p'))
            timePair["end"] = (time.strptime('September 3 1969 ' + k["end_time"], '%B %d %Y %I:%M%p'))
            t2.append(timePair)
                
        if "Th" in k["days"]:
            timePair = {"start":0,"end":0}
            timePair["start"] = (time.strptime('September 4 1969 ' + k["start_time"], '%B %d %Y %I:%M%p'))
            timePair["end"] = (time.strptime('September 4 1969 ' + k["end_time"], '%B %d %Y %I:%M%p'))
            t2.append(timePair)
                
        if "F" in k["days"]:
            timePair = {"start":0,"end":0}
            timePair["start"] = (time.strptime('September 5 1969 ' + k["start_time"], '%B %d %Y %I:%M%p'))
            timePair["end"] = (time.strptime('September 5 1969 ' + k["end_time"], '%B %d %Y %I:%M%p'))
            t2.append(timePair)
            
            
    #Go through all dates and compare
    for date_1 in t1:
        for date_2 in t2:
            #print(min(date_1["end"],date_2["end"]))
            #delta = min(date_1["end"],date_2["end"]) - max(date_1["start"],date_2["start"])
            delta = (time.mktime(min(date_1["end"],date_2["end"])) - time.mktime(max(date_1["start"],date_2["start"]))) / 60
            #
            # Check if delta is negative, 
            #
            if not (delta <= 0):
               collides = True
            else:
                collides = False
                
    
    return collides
    
def getSections(course):
    #print course
    courses = []
    request = requests.get("http://api.umd.io/v0/courses/" + course)
    parsedJson = request.json()
    for section in parsedJson["sections"]:
            courses.append(section)
    return courses

def getCoursesWithSections(myClasses):
    coursesWithSections = []
    for x in myClasses:
        #print "Sec is "+x
        coursesWithSections.append(getSections(x))
        
    return coursesWithSections

def findWorkingClasses():
    listOfSchedule = getCoursesWithSections(allClasses)
    
    classesThatWork = []
    combinationsThatWork = []
    
    #print listOfSchedule
    
    for currentClass in range(1):
        for section in range(len(listOfSchedule[currentClass])):
            for section2 in range(len(listOfSchedule[currentClass+1])):
                if not(doesCollide(listOfSchedule[currentClass][section], listOfSchedule[currentClass+1][section2])):
                    classesThatWork.append(listOfSchedule[currentClass][section])
                    classesThatWork.append(listOfSchedule[currentClass+1][section2])
                    combinationsThatWork.append(classesThatWork)
                    classesThatWork = []
    
    largeArr = []
    
    for i in listOfSchedule[2:]:
        for j in i:
            for a in combinationsThatWork:
                flag = True
                for b in a:
                    if flag and not doesCollide(j,b):
                        temp = a
                        temp.append(j)
                        if(len(temp) == 4):
                            del temp[-1]
                        if temp not in largeArr:
                            largeArr.append(temp)
                    else:
                        flag = False
                        
    
    for i in listOfSchedule[3:]:
        for j in i:
            for a in combinationsThatWork:
                flag = True
                for b in a:
                    if flag and not doesCollide(j,b):
                        temp = a
                        temp.append(j)
                        if(len(temp) == 5):
                            del temp[-1]
                        if temp not in largeArr:
                            largeArr.append(temp)
                    else:
                        flag = False
    
    for i in listOfSchedule[4:]:
        for j in i:
            for a in combinationsThatWork:
                flag = True
                for b in a:
                    if flag and not doesCollide(j,b):
                        temp = a
                        temp.append(j)
                        if(len(temp) == 6):
                            del temp[-1]
                        if temp not in largeArr:
                            largeArr.append(temp)
                    else:
                        flag = False
    
    return largeArr

def sendEvents(final):
    schedule = final[0]
    resultsArr = []
    
    for section in schedule:
        #courseDict[section]
        request = requests.get("http://api.umd.io/v0/courses/sections/" + section)
        parsedJson = request.json()
        meetings = parsedJson["meetings"]
        for meetingDay in meetings:
            eventDict = {}
            eventDict["id"] = len(resultsArr)
            eventDict["text"] = section + " " + meetingDay["classtype"]
            if "M" in meetingDay["days"]: 
                meetingTime = time.strptime("February 24 2014 "+meetingDay["start_time"], '%B %d %Y %I:%M%p')
                eventDict["start"] = time.strftime('%Y-%m-$dT%H:%M:%S',meetingTime)
                meetingTime = time.strptime("February 24 2014 "+meetingDay["end_time"], '%B %d %Y %I:%M%p')
                eventDict["end"] = time.strftime('%Y-%m-$dT%H:%M:%S',meetingTime)
                resultsArr.append(eventDict.copy())
                eventDict.pop("start")
                eventDict.pop("end")
            if "Tu" in meetingDay["days"]: 
                meetingTime = time.strptime("February 25 2014 "+meetingDay["start_time"], '%B %d %Y %I:%M%p')
                eventDict["start"] = time.strftime('%Y-%m-$dT%H:%M:%S',meetingTime)
                meetingTime = time.strptime("February 25 2014 "+meetingDay["end_time"], '%B %d %Y %I:%M%p')
                eventDict["end"] = time.strftime('%Y-%m-$dT%H:%M:%S',meetingTime)
                resultsArr.append(eventDict.copy())
                eventDict.pop("start")
                eventDict.pop("end")
            if "W" in meetingDay["days"]: 
                meetingTime = time.strptime("February 26 2014 "+meetingDay["start_time"], '%B %d %Y %I:%M%p')
                eventDict["start"] = time.strftime('%Y-%m-$dT%H:%M:%S',meetingTime)
                meetingTime = time.strptime("February 26 2014 "+meetingDay["end_time"], '%B %d %Y %I:%M%p')
                eventDict["end"] = time.strftime('%Y-%m-$dT%H:%M:%S',meetingTime)
                resultsArr.append(eventDict.copy())
                eventDict.pop("start")
                eventDict.pop("end")
            if "Th" in meetingDay["days"]: 
                meetingTime = time.strptime("February 27 2014 "+meetingDay["start_time"], '%B %d %Y %I:%M%p')
                eventDict["start"] = time.strftime('%Y-%m-$dT%H:%M:%S',meetingTime)
                meetingTime = time.strptime("February 27 2014 "+meetingDay["end_time"], '%B %d %Y %I:%M%p')
                eventDict["end"] = time.strftime('%Y-%m-$dT%H:%M:%S',meetingTime)
                resultsArr.append(eventDict.copy())
                eventDict.pop("start")
                eventDict.pop("end")   
            if "F" in meetingDay["days"]: 
                meetingTime = time.strptime("February 28 2014 "+meetingDay["start_time"], '%B %d %Y %I:%M%p')
                eventDict["start"] = time.strftime('%Y-%m-$dT%H:%M:%S',meetingTime)
                meetingTime = time.strptime("February 28 2014 "+meetingDay["end_time"], '%B %d %Y %I:%M%p')
                eventDict["end"] = time.strftime('%Y-%m-$dT%H:%M:%S',meetingTime)
                resultsArr.append(eventDict.copy())
                eventDict.pop("start")
                eventDict.pop("end")
                
    return resultsArr
    
def filterLeastWalking(home):
    possibleSchedules = finalSchedules
    print finalSchedules
    homeLat = ""
    homeLon = ""
    destLat = ""
    destLon = ""
    distanceWalked = 1000000000
    leastWalking = []
    leastWalkingDict = {}
    bestSchedules = {}
    
    
    request = requests.get("http://api.umd.io/v0/map/buildings")
    parsedJson = request.json()
    for buildingInfo in parsedJson:
        if home in buildingInfo["name"]:
            homeLat = buildingInfo["lat"]
            homeLon = buildingInfo["lng"]
    
    for schedule in possibleSchedules:
        distanceForSchedule = 0;
        for section in schedule:
            meetings = courseDict[section]["meetings"]
            distanceForSection = 0
            for meeting in meetings:
                numberOfMeetings = 0
                days = meeting["days"]
                if "M" in days:
                    numberOfMeetings += 1
                if "Tu" in days:
                    numberOfMeetings += 1
                if "W" in days:
                    numberOfMeetings += 1
                if "Th" in days:
                    numberOfMeetings += 1
                if "F" in days:
                    numberOfMeetings += 1
                dest = meeting["building"]
                request = requests.get("http://api.umd.io/v0/map/buildings")
                parsedJson = request.json()
                for buildingInfo in parsedJson:
                    if dest in buildingInfo["code"]:
                        destLat = buildingInfo["lat"]
                        destLon = buildingInfo["lng"]
                tempURL = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=" + str(homeLat) + "," + str(homeLon) + "&destinations=" + str(destLat) + "," + str(destLon) + "&mode=walking&key=AIzaSyC2nDuCufXk8w8112AKKiNXcLymkxcZk7Q"
                request = requests.get(tempURL)
                parsedJson = request.json()
                distanceForSection += int(parsedJson['rows'][0]['elements'][0]['distance']['value']) * numberOfMeetings
                #print str(section) + ", you are walking " + str(parsedJson['rows'][0]['elements'][0]['distance']['value']) + " " + str(numberOfMeetings)
            distanceForSchedule += distanceForSection
        if distanceForSection < distanceWalked:
            distanceWalked = distanceForSection
            leastWalking = schedule
        leastWalkingDict[distanceForSchedule] = schedule
    
    lowest = 10000000
    counter = 0
    while(counter <= len(leastWalkingDict.keys())):
        for key in leastWalkingDict.keys():
            if(key < lowest):
                lowest = key
        bestSchedules[counter] = leastWalkingDict.pop(lowest)
        counter+=1
        lowest = 10000000
        
    return leastWalkingDict

def filterLatest(pref):
    likeMorning = pref
    possibleSchedules = finalSchedules
    scoredTimes = []
    baseVal = time.mktime(time.strptime('September 3 1969 8:00am', '%B %d %Y %I:%M%p'))-time.mktime(time.strptime('September 1 1969 8:00am', '%B %d %Y %I:%M%p'));
    
    for schedule in possibleSchedules:
        timeScoreForSchedule={"M":baseVal,"Tu":baseVal,"W":baseVal,"Th":baseVal,"F":baseVal}
        for section in schedule:
            meetings = courseDict[section]["meetings"]
            distanceForSection = 0
            for meeting in meetings:
                numberOfMeetings = 0
                days = meeting["days"]
                if "M" in days:
                    startTime = (time.strptime('September 1 1969 ' + meeting["start_time"], '%B %d %Y %I:%M%p'))
                    baseTime = (time.strptime('September 1 1969 8:00am', '%B %d %Y %I:%M%p'))
                    delta = time.mktime(startTime) - time.mktime(baseTime)
                    if timeScoreForSchedule["M"]>delta:
                        timeScoreForSchedule["M"]=delta
                if "Tu" in days:
                    startTime = (time.strptime('September 1 1969 ' + meeting["start_time"], '%B %d %Y %I:%M%p'))
                    baseTime = (time.strptime('September 1 1969 8:00am', '%B %d %Y %I:%M%p'))
                    delta = time.mktime(startTime) - time.mktime(baseTime)
                    if timeScoreForSchedule["Tu"]>delta:
                        timeScoreForSchedule["Tu"]=delta
                if "W" in days:
                    startTime = (time.strptime('September 1 1969 ' + meeting["start_time"], '%B %d %Y %I:%M%p'))
                    baseTime = (time.strptime('September 1 1969 8:00am', '%B %d %Y %I:%M%p'))
                    delta = time.mktime(startTime) - time.mktime(baseTime)
                    if timeScoreForSchedule["W"]>delta:
                        timeScoreForSchedule["W"]=delta
                if "Th" in days:
                    startTime = (time.strptime('September 1 1969 ' + meeting["start_time"], '%B %d %Y %I:%M%p'))
                    baseTime = (time.strptime('September 1 1969 8:00am', '%B %d %Y %I:%M%p'))
                    delta = time.mktime(startTime) - time.mktime(baseTime)
                    if timeScoreForSchedule["Th"]>delta:
                        timeScoreForSchedule["Th"]=delta
                if "F" in days:
                    startTime = (time.strptime('September 1 1969 ' + meeting["start_time"], '%B %d %Y %I:%M%p'))
                    baseTime = (time.strptime('September 1 1969 8:00am', '%B %d %Y %I:%M%p'))
                    delta = time.mktime(startTime) - time.mktime(baseTime)
                    if timeScoreForSchedule["F"]>delta:
                        timeScoreForSchedule["F"]=delta
        #print "For " + str(section) + " you have walked " + str(distanceForSection)
        numDays = 0
        totalVal = 0
            
        for dayTime in timeScoreForSchedule:
            if not dayTime == baseVal:
                numDays+=1
                totalVal+=timeScoreForSchedule[dayTime]
            
                
        scoredTimes.append({"time":totalVal/numDays,"sched":schedule})
    
    bestScore = time.mktime(time.strptime('September 1 1969 7:00am', '%B %d %Y %I:%M%p'))-time.mktime(time.strptime('September 1 1969 8:00am', '%B %d %Y %I:%M%p'))
    bestSchedule = {}
    sortedBest = {}
    count = 0
    
    for scorePair in scoredTimes:
        #print str(scorePair["time"])
        #print str(scorePair)+str(time.strftime('%H:%M:%S', time.gmtime(scorePair["time"]))
        bestSchedule[scorePair["time"]] = scorePair["sched"]
        
        for key in sorted(bestSchedule.iterkeys()):
            sortedBest[count] = key["sched"]
                
    convertedTime = time.strftime('%H:%M:%S', time.gmtime(bestScore+28800.0))           
    
    return sortedBest
    
    
def filterNoSchool(day):
    desiredDayOff = day
    possibleSchedules = finalSchedules
    validTimes = []
    
    for schedule in possibleSchedules:
        timeScoreForSchedule={"M":True,"Tu":True,"W":True,"Th":True,"F":True}
        for section in schedule:
            #courseDict[section]
            request = requests.get("http://api.umd.io/v0/courses/sections/" + section)
            parsedJson = request.json()
            meetings = parsedJson["meetings"]
            distanceForSection = 0
            for meeting in meetings:
                numberOfMeetings = 0
                days = meeting["days"]
                if "M" in days:
                    timeScoreForSchedule["M"]=False
                if "Tu" in days:
                    timeScoreForSchedule["Tu"]=False
                if "W" in days:
                    timeScoreForSchedule["W"]=False
                if "Th" in days:
                    timeScoreForSchedule["Th"]=False
                if "F" in days:
                    timeScoreForSchedule["F"]=False
                    
        hasOff = timeScoreForSchedule[desiredDayOff]
                
        validTimes.append({"hasDayOff":hasOff,"sched":schedule})
    
    possibleSchedules={}
    
    for scorePair in validTimes:
        #print "Day off found with following schedule: " + str(scorePair)
        possibleSchedules[len(possibleSchedules)]=scorePair["sched"]
        
    return possibleSchedules
    
def mainAlgorithm(data):
    #Load classes
    #allClasses = data["classes"]
    #print allClasses
    #First find all valid combinations of sections
    finalSchedules = findWorkingClasses()
    print len(finalSchedules)
    #Check and apply needed filters
    if(data["walking"] is "true"):
        finalSchedules = filterLeastWalking(data["building"])
        
    if(data["day"] is "true"):
        finalSchedules = filterNoSchool(data["day-selected"])
        
    if(data["morning"] is "true"):
        finalSchedules = filterLatest(True)
        
    if(data["afternoon"] is "true"):
        finalSchedules = filterLatest(False)
        
    #Push data to server
    return sendEvents(finalSchedules)
    
 

#print main(data)