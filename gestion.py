
import json
from tqdm import tqdm
from pprint import pprint
import urllib
#from urllib2 import urlopen
import datetime
#import urllib3



def AddPersonToData(idd, FirstName, SecondName, Fonction, Link):#add a person of the data
	try:
		with open('database.json', 'r') as f:
			 data = json.load(f)
		data["Person"][idd] = {
				"FirstName": FirstName,
				"SecondName": SecondName,
				"Fonction": Fonction,
				"Link": Link,
				"InEsilv": "No" 
			}
		with open('database.json', 'w') as f:
			 json.dump(data, f, indent = 4)
	except :
		print("Input data invalid (AddPersonToData)")


def DeletePersonToData(idd):#delete a person of the data
	try:
		with open('database.json', 'r') as f:
			 data = json.load(f)
		del data["Person"][idd]
		with open('database.json', 'w') as f:
			 json.dump(data, f, indent = 4)
	except :
		print("Input id invalid (DeletePersonToData)")

def returnTxtWithUrl(url):# convert the irl into txt
	content=urllib.urlopen(url)
	ToReturn = []
	print("Telechargement lien")
	for line in tqdm(content):
		ToReturn.append(str(line))
	return ToReturn

def scheduleWithIdd(idd):# return all the schredul with the ID
	try:
		with open('database.json', 'r') as f:
			 data = json.load(f)
		txt = returnTxtWithUrl(data["Person"][idd]["Link"])
		Start = 0
		date = []
		place = ""
		group = ""
		schredul = []
		for line in txt:
			if "BEGIN:VEVENT" in line:
				Start = 1
			if "END:VEVENT" in line:
				Start = 0
				date = []
				place = ""
				group = ""
			if "UID" in line:
				try:
					date = [int(line.split("-")[1]), int(line.split("-")[2]), int(line.split("-")[3]), line.split("-")[4]] #[years, month, day, hour]
					date[3] = int(date[3].split(":")[0]), date[3].split(":")[1]
				except :
					date = []
			if "LOCATION" in line:
				place = line.split(":")[1]
				place = place.split("\\")[0]
			if "GROUPE" in line:
				group = line
			if Start == 1 and date != [] and place != "" and group != "":
				schredul.append([date, place, group])
				Start = 0
		return (schredul)
	except :
		print("Link or id invalid (scheduleWithIdd)")
		

"""
def NextCours(idd):# return the next cours with the ID
	try:
		test = scheduleWithIdd(idd)
		#print(test)
		dateActuelle = datetime.datetime.now()
		cours = []
		for index in test:
			if index[0][0] == int(dateActuelle.year) and index[0][1] == int(dateActuelle.month) and index[0][2] == int(dateActuelle.day):
				cours.append(index)
		#print(cours)
		if dateActuelle.minute<10:
			hourmin = int(str(dateActuelle.hour) + "0" + str(dateActuelle.minute))
		else :
			hourmin = int(str(dateActuelle.hour) + str(dateActuelle.minute))
		for index in cours:
			if int(str(index[0][3][0]) + index[0][3][1]) > hourmin - 50 :
				nextCours = index
				return nextCours
	except :
		print("Probleme (NextCours)")
"""

def NextCours(idd):# return the next cours with the ID
	try:
		test = scheduleWithIdd(idd)
		#print(test)
		dateActuelle = datetime.datetime.now()
		cours = []
		for index in test:
			if index[0][0] == int(dateActuelle.year) and index[0][1] == int(dateActuelle.month) and index[0][2] == 21:
				cours.append(index)
		#print(cours)

		hourmin = int(str(dateActuelle.hour) + str(dateActuelle.minute))
		#print(hourmin)
		for index in cours:
			if int(str(index[0][3][0]) + index[0][3][1]) > 800 :
				nextCours = index
				return nextCours
	except :
		print("Probleme (NextCours)")

def PresentWithId(idd):
	try:
		with open('database.json', 'r') as f:
			 data = json.load(f)
		data["Person"][idd]["InEsilv"] = "Yes"
		with open('database.json', 'w') as f:
			 json.dump(data, f, indent = 4)
	except :
		print("Input data invalid (PresentWithId)")

def ClearInEsilv():
	try:
		with open('database.json', 'r') as f:
			 data = json.load(f)
		for index in data["Person"]:
			data["Person"][index]["InEsilv"] = "No"
		with open('database.json', 'w') as f:
			 json.dump(data, f, indent = 4)
	except :
		print("Error (ClearInEsilv)")

def listStudentPresentInCoursWithId(idd):
	try:
		main = NextCours(idd)
		if main == None:
			return None
		list1 = []
		with open('database.json', 'r') as f:
			 data = json.load(f)
		for index in data["Person"]:
			data["Person"][index]["InEsilv"]
			if NextCours(index) == main and data["Person"][index]["InEsilv"] == "No" and data["Person"][index]["Fonction"] == "Student":
				list1.append(str(data["Person"][index]["FirstName"]) + " " + str(data["Person"][index]["SecondName"]))
		return list1
	except :
		print("Error (listStudentCoursWithId)")

#print(NextCours("00003"))
#ClearInEsilv()
#print(listStudentPresentInCoursWithId("00003"))

#print(scheduleWithIdd("00004"))
#PresentWithId("00003")
#PresentWithId("00002")
#ClearInEsilv()
