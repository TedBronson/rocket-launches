import requests as r
import math
import encodings

from dask.compatibility import FileNotFoundError

import rocket_launches
import smtplib
import rocket_launches_in_period


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
    message_constructed = 'Subject: Rocket launches for today \n'
    message_constructed += 'In next 3 days we are expecting following launches: \n \n'
    message_constructed += message

    # Send a message
    to_email = content[2]
    server.sendmail(from_email, to_email, message_constructed)
    print(message_constructed)

    server.quit()


def main():
    # if rocket_launches_in_period.verify_launches_will_happen() is True:
    launches_tomorrow_message = rocket_launches_in_period.compose_message_for_upcoming_launches(rocket_launches_in_period.launches_in_period())
    send_email(launches_tomorrow_message)

main()
