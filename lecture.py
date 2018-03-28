import RPi.GPIO as GPIO
import MFRC522
import signal
import ecran
#import test

# Create an object of the class MFRC522
MIFAREReader = MFRC522.MFRC522()

def lecture():

    # Scan for cards
    (status,TagType) = MIFAREReader.MFRC522_Request(MIFAREReader.PICC_REQIDL)
    id = "None"
    # If a card is found
    if status == MIFAREReader.MI_OK:
        print "Card detected"

    # Get the UID of the card
    (status,uid) = MIFAREReader.MFRC522_Anticoll()
    #ecran.afficher(str(uid[0]))
    # If we have the UID, continue
    if status == MIFAREReader.MI_OK:

        # Print UID
        #print "Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])
      	id = str(uid[0])+str(uid[1])+str(uid[2])+str(uid[3])
	print("lecture id " + id)
	#ecran.afficher(str(uid[0]))
        # This is the default key for authentication
        key = [0xFF,0xFF,0xFF,0xFF,0xFF,0xFF]

        # Select the scanned tag
        MIFAREReader.MFRC522_SelectTag(uid)

        # Authenticate
        status = MIFAREReader.MFRC522_Auth(MIFAREReader.PICC_AUTHENT1A, 8, key, uid)

        # Check if authenticated
        if status == MIFAREReader.MI_OK:
            MIFAREReader.MFRC522_Read(8)
            MIFAREReader.MFRC522_StopCrypto1()
        else:
            print "Authentication error"
    return id
