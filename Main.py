
#!/usr/bin/env python
# -*- coding: utf8 -*-

import RPi.GPIO as GPIO
import MFRC522
import signal
import ecran
import lecture
import gestion
from time import *

continue_reading = True

# Capture SIGINT for cleanup when the script is aborted
def end_read(signal,frame):
    global continue_reading
    print "Ctrl+C captured, ending read."
    continue_reading = False
    GPIO.cleanup()

# Hook the SIGINT
signal.signal(signal.SIGINT, end_read)

# Create an object of the class MFRC522
#MIFAREReader = MFRC522.MFRC522()

# Welcome message
print "Welcome to the MFRC522 data read example"
print "Press Ctrl-C to stop."

#Mettre absent tout le monde pour la journee
gestion.ClearInEsilv()

# This loop keeps checking for chips. If one is near it will get the UID and authenticate
while continue_reading:
	#ecran.afficher("Presenter Carte")
	print("Presenter la Carte")
	uid = lecture.lecture()
	#print("id carte est " +str(id_carte))
	if(uid != "None"):
		id_carte = str(uid)
		gestion.PresentWithId(id_carte)
		#print("l eleve est present")
		horaire = gestion.NextCours(id_carte)
		if horaire == []:
			ecran.afficher("Pas cours")
		else:
			show = str(horaire[0][3][0])+"H" + str(horaire[0][3][1])+" en "+str(horaire[1]+"  ")
			ecran.afficher(show)
			print(show)
		

