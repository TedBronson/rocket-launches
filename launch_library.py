from dask.compatibility import FileNotFoundError

import smtplib
import rocket_launches_in_period
from email.mime.text import MIMEText


def send_email(message):
    message = message.encode('utf8')
    # connect to the smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')
    server.starttls()

    try:
        with open('email.txt', 'r') as f:
            content = f.readlines()

    except FileNotFoundError as err:
        print(err)

    # Login
    password = content[1]
    from_email = content[0]
    server.login(from_email, password)

    # Compose a message
    message_constructed = 'In next 3 days we are expecting following launches: \n \n'
    message_constructed += message

    msg = MIMEText(message_constructed)
    msg['Subject'] = 'Rocket launches for today'
    msg['From'] = from_email

    # Send a message
    to_email = content[2]
    server.sendmail(from_email, to_email, msg.as_string())
    print(msg.as_string())

    server.quit()


def main():
    # if rocket_launches_in_period.verify_launches_will_happen() is True:
    launches_tomorrow_message = rocket_launches_in_period.compose_message_for_upcoming_launches(rocket_launches_in_period.launches_in_period())
    send_email(launches_tomorrow_message)

main()
