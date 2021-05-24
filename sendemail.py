import smtplib
from email.message import EmailMessage
def usermail(TEXT,tomail):
    msg = EmailMessage()
    msg['Subject'] = 'Complaint Registered | Customer Care Registry'
    msg['From'] = 'apekshab9616@gmail.com'
    msg['To'] = tomail
    msg.set_content('')
    msg.add_alternative(TEXT,subtype='html')


    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('apekshab9616@gmail.com','9900569616appi')
        smtp.send_message(msg)
        

def agentmail(TEXT,tomail):
    msg = EmailMessage()
    msg['Subject'] = 'New Complaint Registered | Customer Care Registry'
    msg['From'] = 'apekshab9616@gmail.com'
    msg['To'] = tomail
    msg.set_content('')
    msg.add_alternative(TEXT,subtype='html')


    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login('apekshab9616@gmail.com','9900569616appi')
        smtp.send_message(msg)

   
