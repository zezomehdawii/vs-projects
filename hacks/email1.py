#test send email app
import smtplib

def send_email(username, password, recipient, subject, body):
    FROM = username
    TO = recipient if isinstance(recipient,list) else [recipient]
    SUBJECT = subject
    TEXT = body
    # prepare the actual email
    message = """From %s\nTO: %s \nSubject: %s\n\n%s
    """ %(FROM, ",".join(TO), SUBJECT, TEXT)
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(username,password)
        server.sendmail(FROM, TO, message)
        server.close()
        print ("[*] Email sent successfully")
    except:
        print("fail to send email") 



username = input("Enter email: ")
password = input("Enter pasword: ")
recipient = input("Enter recipient email: ")
subject = input("Enter subject: ")
body = input("Enter message: ")
send_email(username, password, recipient, subject, body)