import requests
import re
from bs4 import BeautifulSoup
def getUserProfileObjectFromUrl(userProfileUrl):
    userObject = {}
    userObject['userProfileLink'] = userProfileUrl
    page=requests.get(userProfileUrl)
    soup = BeautifulSoup(page.content, 'html.parser')
    allTDs = soup.table.find_all('td')
    for i in range(len(allTDs)):
        text = (allTDs[i].string or "").strip()
        if text == "GRE":
            userObject['greQ'] = (allTDs[i+2].string or "").strip()
            userObject['greV'] = (allTDs[i+4].string or "").strip()
            userObject['greA'] = (allTDs[i+6].string or "").strip()
            i += 6
        if text == "TOEFL":
            userObject['toeflScore'] = (allTDs[i+2].string or "").strip()
            i += 2
        if text == "Grade":
            userObject['cgpa'] = (allTDs[i+1].string or "").strip()
            i += 2
        if text == "Grade Scale":
            userObject['cgpaScale'] = (allTDs[i+1].string or "").strip()
            i += 2

        #filling default values for missing values

        if "greQ" not in userObject:
            userObject['greQ'] = "0"
        if "greV" not in userObject:
            userObject['greV'] = "0"
        if "greA" not in userObject:
            userObject['greA'] = "0"
        if "toeflScore" not in userObject:
            userObject['toeflScore'] = "0"
        if "cgpa" not in userObject:
            userObject['cgpa'] = "0"
        if "cgpaScale" not in userObject:
            userObject['cgpaScale'] = "0"
    return userObject

for userInfo in open("Users.txt"):
    userName, userLink = userInfo.split(",")
    vals = []
    userInfoObj = getUserProfileObjectFromUrl(userLink)
    for key in userInfoObj:
        vals.append(userInfoObj[key])
print("Fetched Information for: ", userLink)
print (userName + "," + str(userInfoObj["toeflScore"]) + "," + str(userInfoObj["greV"]) + "," + str(userInfoObj["greQ"]) + "," +str(userInfoObj["greA"]) )
userInfoJSON.write(userName + "," + userInfoObj["toeflScore"]+ "," + str(userInfoObj["greV"]) + "," + str(userInfoObj["greQ"]) + "," + userInfoObj["greA"])
