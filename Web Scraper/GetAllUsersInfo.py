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
        if text == "Program":
            userObject['program'] = (allTDs[i+1].string or "").strip()
            i += 2
        if text == "Major":
            userObject['major'] = (allTDs[i+1].string or "").strip()
            i += 2
        if text == "Specialization":
            userObject['specialization'] = (allTDs[i+1].string or "").strip()
            i += 2
        if text == "Term and Year":
            userObject['termAndYear'] = (allTDs[i+1].string or "").strip()
            i += 2
        if text == "GRE":
            userObject['greQ'] = (allTDs[i+2].string or "").strip()
            userObject['greV'] = (allTDs[i+4].string or "").strip()
            userObject['greA'] = (allTDs[i+6].string or "").strip()
            i += 6
        if text == "GMAT":
            userObject['gmatQ'] = (allTDs[i+2].string or "").strip()
            userObject['gmatV'] = (allTDs[i+4].string or "").strip()
            userObject['gmatA'] = (allTDs[i+6].string or "").strip()
            i += 6
        if text == "TOEFL":
            userObject['toeflScore'] = (allTDs[i+2].string or "").strip()
            userObject['toeflEssay'] = (allTDs[i+4].string or "").strip()
            i += 4
        if text == "University/College":
            userObject['ugCollege'] = (allTDs[i+1].string or "").strip()
            i += 2
        if text == "Department":
            userObject['department'] = (allTDs[i+1].string or "").strip()
            i += 2
        if text == "Grade":
            userObject['cgpa'] = (allTDs[i+1].string or "").strip()
            i += 2
        if text == "Topper's Grade":
            userObject['topperCgpa'] = (allTDs[i+1].string or "").strip()
            i += 2
        if text == "Grade Scale":
            userObject['cgpaScale'] = (allTDs[i+1].string or "").strip()
            i += 2
        if text == "Journal Publications":
            userObject['journalPubs'] = (allTDs[i+1].string or "").strip()
            i += 2
        if text == "Conference Publications":
            userObject['confPubs'] = (allTDs[i+1].string or "").strip()
            i += 2
        if text == "Industrial Experience":
            val = (allTDs[i+1].string or "").strip()
            userObject['industryExp'] = yearToMonths(val)
            i += 2
        if text == "Research Experience":
            val = (allTDs[i+1].string or "").strip()
            userObject['researchExp'] = yearToMonths(val)
            i += 2
        if text == "Internship Experience":
            val = (allTDs[i+1].string or "").strip()
            userObject['internExp'] = yearToMonths(val)
            i += 2



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

propertyList = ["userName","major","researchExp","industryExp","specialization","toeflScore",
                "program","department","toeflEssay","internExp","greV","greQ","userProfileLink",
                "journalPubs","greA","topperCgpa","termAndYear","confPubs","ugCollege","gmatA","cgpa","gmatQ","cgpaScale","gmatV"]
userInfoJSON = open("allUsers.csv", "w")
count = 0
userInfoJSON.write(','.join(propertyList) + "\n")
for userInfo in open("uniqueUsers.txt"):
    userName, userLink = userInfo.split(",")
    vals = []
    userInfoObj = getUserProfileObjectFromUrl(userLink)
    for key in userInfoObj:
        vals.append(userInfoObj[key])
    print(Fetched Information for: ", userLink, ",", userName)
    print(userName + "," + userInfoObj["major"].replace(",", " ") + "," + str(userInfoObj["researchExp"]) + "," + str(userInfoObj["industryExp"]) + "," + userInfoObj["specialization"].replace(",", " ") + "," + str(userInfoObj["toeflScore"]) + "," + userInfoObj["program"] + "," + userInfoObj["department"] + "," + str(userInfoObj["toeflEssay"]) + "," + str(userInfoObj["internExp"]) + "," + str(userInfoObj["greV"]) + "," + str(userInfoObj["greQ"]) + "," + userInfoObj["userProfileLink"].strip() + "," + str(userInfoObj["journalPubs"]) + "," + str(userInfoObj["greA"]) + "," + str(userInfoObj["topperCgpa"]) + "," + userInfoObj["termAndYear"] + "," + str(userInfoObj["confPubs"]) + "," + userInfoObj["ugCollege"].replace(",", " ") + "," + str(userInfoObj["gmatA"]) + "," + str(userInfoObj["cgpa"]) + "," + str(userInfoObj["gmatQ"]) + "," + str(userInfoObj["cgpaScale"]) + "," + str(userInfoObj["gmatV"]))
    userInfoJSON.write(userName + "," + userInfoObj["major"].replace(",", " ") + "," + str(userInfoObj["researchExp"]) + "," + str(userInfoObj["industryExp"]) + "," + userInfoObj["specialization"].replace(",", " ") + "," + str(userInfoObj["toeflScore"]) + "," + userInfoObj["program"] + "," + userInfoObj["department"] + "," + str(userInfoObj["toeflEssay"]) + "," + str(userInfoObj["internExp"]) + "," + str(userInfoObj["greV"]) + "," + str(userInfoObj["greQ"]) + "," + userInfoObj["userProfileLink"].strip() + "," + str(userInfoObj["journalPubs"]) + "," + str(userInfoObj["greA"]) + "," + str(userInfoObj["topperCgpa"]) + "," + userInfoObj["termAndYear"] + "," + str(userInfoObj["confPubs"]) + "," + userInfoObj["ugCollege"].replace(",", " ") + "," + str(userInfoObj["gmatA"]) + "," + str(userInfoObj["cgpa"]) + "," + str(userInfoObj["gmatQ"]) + "," + str(userInfoObj["cgpaScale"]) + "," + str(userInfoObj["gmatV"]))
    userInfoJSON.write("\n")

    count += 1

    print("Count so far: ", count)
userInfoJSON.close()
