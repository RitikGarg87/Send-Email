from getpass import getpass
import smtplib , webbrowser
def get_mail():
    serviceAvailable = ['hotmail','gmail','yahoo','outlook']
    while True:
        mail_id = input("e_mail:")
        if '@' in mail_id and '.com' in mail_id:
            symbol_pos = mail_id.find("@")
            dotcom_pos = mail_id.find(".com")
            sp = mail_id[symbol_pos+1:dotcom_pos]
            if sp in serviceAvailable:
                return mail_id , sp
                break
            else:
                  print("we dont provide service for" + sp)
                  print("we provide  service only for : hotmail/outlook,yahoo,gmail")
                  continue
        else:
            print("invalid e_mail retype again")
            continue
def set_smtp_domain(serviceProvider):
     if serviceProvider == 'gmail':
            return 'smtp.gmail.com'
     elif serviceProvider == 'outlook' or serviceProvider == 'hotmail':
            return 'smtp-mail.outlook.com'
     elif serviceProvider == 'yahoo':
            return 'smtp.mail.yahoo.com'
        
print("u can send e-mail by this program")
print("please enter ur e-mail and password: ")
e_mail , serviceProvider = get_mail()
password = getpass("password: ")
while True:
       try:
            smtpDomain = set_smtp_domain(serviceProvider)
            connection = smtplib.SMTP(smtpDomain)
            connection.ehlo()
            connection.starttls()
            connection.login(e_mail , password)
       except:
            if serviceProvider == 'gmail':
                print('login unseccussfull:')
                print('you typed wrong detail')
                print('do u want to open web page')
                answer = input("yes or no: ")
                if answer == 'yes' :
                    webbrowser.open("https://myaccount.google.com/lesssecureapps")
                else:
                    print("we won't open webpage for u ")
                print("please retype ur e-mail and password also")
                e_mail ,  serviceProvider = get_mail()
                password = getpass("password: ")
                continue
            else:
                print("login unsuccessfull , most possible u typed wrong username and password ")
                print("please retype ur e-mail address and password ")
                e_mail ,  serviceProvider = get_mail()
                password = getpass("password: ")
                continue
       else:
           print("login successfull ")
           break
print("please type receiver's E-mail address ")
receiverAddress , receiverSP = get_mail()
print("now please type subject and message ")
Subject = input("Subject: ")
Message = input("Message: ")
connection.sendmail(e_mail , receiverAddress , ("Subject: " + str(Subject) + "\n\n" + str(Message)))
print("E-mail send successfully ")
connection.quit()

        






















                        
                    
                    
                
             
