from statistics import median  # this is to get the median. 
from datetime import date
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta
from bs4 import BeautifulSoup
import requests
 
 
def getLongDiff(date1, date2=date.today()):
    delta = relativedelta(date1, date2)
    return "{} years, {} months, {} days".format(delta.years, delta.months, delta.days)
 
 
def getAge(birthday, compDate=date.today()):
    ageDays = compDate - birthday   # subtract today from their birthday to get a timedelta object
    age = getLongDiff(compDate, birthday)
    return age, ageDays.days
 
 
def daysToYears(days):
    return days / 364.2425
 
 
url = "https://www.tdcj.state.tx.us/death_row/dr_offenders_on_dr.html"
 
doc = BeautifulSoup(requests.get(url).text, 'html.parser') # brings back text from html and uses the html.parser
 
# Our rows look like this:
# [ID,  Link,   LastName,   FirstName,  Birthdate,  Sex,    Race,   RecvDate,   County,     OffenseDate]
# [0,   1,      2,          3,          4,          5,      6,      7,          8,          9          ]
inmateDict = {}
for i in doc.find_all('table', attrs={'id': 'inmate_table'})[1:]:
    iDict = {}
 # created a dictionary, and assigned the value of it as another dictionary.
    columns = i.find_all('td')
    iDict['readableAge'], iDict['ageDays'] = getAge(
        parse(columns[4].text).date())
 
    iDict['timeOn'] = (date.today() - parse(columns[7].text).date()).days
    iDict['daysBetween'] = (
        parse(columns[7].text).date() - parse(columns[9].text).date()).days
 
    inmateDict[columns[0].text] = iDict 
medTimeOn = median([i['timeOn'] for i in inmateDict.values()]) # for every object in value, gets the time on value and adds it to a list. The median needs to take a list. 
# lines 47-50 do the same as line 45
#timeOnList = []
#for i in inmateDict.values():
    #timeOnList.append(i['timeOn'])
    #medTimeOn = median(timeOnList)  

# avgTimeOn = sum(
#     i['timeOn'] for i in inmateDict.values()
# ) / len(inmateDict)
 
oldest = max(
    inmateDict.values(),
    key=lambda i: i['ageDays'] # acts like a for loop 
)
 
medSent = median([i['daysBetween'] for i in inmateDict.values()])
# avgSent = sum(
#     i['daysBetween'] for i in inmateDict.values()
# ) / len(inmateDict)
 
print("There are currently {} inmates on death row in Texas.".format(
    len(inmateDict)))
print("The oldest individual on death row is {} old.".format(
    oldest['readableAge']))
print("The median time spent on death row is {:.2f} years.".format(
    daysToYears(medTimeOn)))
print("The median time from crime to sentencing is {:.2f} years.".format(
    daysToYears(medSent)))