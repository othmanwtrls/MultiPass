import gestion
import mail


while(1):
	id = raw_input("id : ")
	email = raw_input("mail : ")
	liste= gestion.listStudentPresentInCoursWithId(id)
	print(liste)
	show=""
	for i in liste:
		show += i+"\n"
	mail.mail(show, email)
	print("Mail envoye")

