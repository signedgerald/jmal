#!/usr/local/bin/python3
from urllib2 import Request, urlopen
import json
import datetime
import sys

date = datetime.datetime.today().weekday()
jikan = 'https://api.jikan.moe/v3'


# def functionSwitch(argString):
#     switcher = {
#         "schedule": schedule(day),
#         "search": search(),
#         "season": seasonalSearch()
#     }
#     return switcher.get(argString)


def switch(date):
    switcher = {
        0: "monday",
        1: "tuesday",
        2: "wednesday",
        3: "thursday",
        4: "friday",
        5: "saturday",
        6: "sunday"
    }
    return switcher.get(date)


def search():
    searchRequest = raw_input('Enter request: ')
    prereq = (jikan + '/search/anime/?q=' + searchRequest + '&limit=5')
    request = Request(prereq)
    response_body = urlopen(request).read()
    parsed_json = json.loads(response_body)
    for result in parsed_json['results']:
        print(result['title'])
        print("Episodes: " + str(result['episodes']))
        print("Score: " + str(result['score']))
    return


def seasonalSearch():
    year = raw_input('Enter year: ')
    season = raw_input('Enter season: ')
    prereq = (jikan + '/season/' + year + '/' + season)
    request = Request(prereq)
    response_body = urlopen(request).read()
    parsed_json = json.loads(response_body)
    for result in parsed_json['anime']:
        print(result['title'])
    # print(response_body)
    return


def schedule(day):
    print("Today's Releases: \n")
    prereq = (jikan + '/schedule/' + day)
    request = Request(prereq)
    response_body = urlopen(request).read()
    parsed_json = json.loads(response_body)
    for day in parsed_json[day]:
        print(day['title'])
    return


print('No. of args', str(sys.argv))

day = switch(date)

if(len(sys.argv) == 1):
    schedule(day)
elif(sys.argv[1] == 'search'):
    search()
elif(sys.argv[1] == 'season'):
    seasonalSearch()
else:
    print("bad input")
