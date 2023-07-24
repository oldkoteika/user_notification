# import necessary packages
import time
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import os
import schedule


from GetData import get_data,update_messag


# create message object instance
def send_messag():
    try:
        msg = MIMEMultipart()

        message = get_data()
        if message:
            msg['From'] = os.environ.get('Email')
            msg['To'] = message.to
            msg['Subject'] = message.subject

            # add in the message body
            msg.attach(MIMEText(message.message, 'plain'))

            #create server
            server = smtplib.SMTP(os.environ.get('SMTP_server'),os.environ.get('SMTP_PORT'))
            server.starttls()

            # Login Credentials for sending the mail
            server.login(msg['From'],os.environ.get('password'))

            # send the message via the server.
            server.sendmail(msg['From'], msg['To'], msg.as_string())
            server.quit()
            update_messag(message,1)
    except Exception as e:
        print(e)
        update_messag(message,-1)

schedule.every(10).seconds.do(send_messag)

while True:
    schedule.run_pending()
    time.sleep(1)




