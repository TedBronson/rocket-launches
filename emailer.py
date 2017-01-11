from dask.compatibility import FileNotFoundError

import smtplib
from email.mime.text import MIMEText


# Function that accepts a message and sends and email.
# TODO: 1. Make send_email function accept subject as argument.
# TODO: 2. Remove all message composition from send_email function
def send_email(message):
    message = message.encode('utf8')
    # connect to the smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')
    server.starttls()

    # Open a file with from_email, password, and to_email.
    try:
        with open('email.txt', 'r') as f:
            content = f.readlines()
    except FileNotFoundError as err:
        print(err)

    # Login
    password = content[1]
    from_email = content[0]
    server.login(from_email, password)

    msg = MIMEText(message)
    msg['Subject'] = 'Rocket launches for today'
    msg['From'] = from_email

    # Send a message
    to_email = content[2]
    server.sendmail(from_email, to_email, msg.as_string())
    print(msg.as_string())

    server.quit()