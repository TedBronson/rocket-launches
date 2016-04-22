import requests as r
import math
import rocket_launches
import smtplib

def send_email(message):
        # connect to the smtp server
    server = smtplib.SMTP('smtp.gmail.com', '587')
    server.starttls()

    try:
        with open('email.txt', 'r') as f:
            content = f.readlines()
                                       
    except FileNotFoundError as err:
        print(err)

    #Login
    password = content[1]
    from_email = content[0]
    server.login(from_email, password)

    #Compose a message
    message_constructed = 'Subject: Rocket launches for today \n'
    message_constructed += 'Today we are expecting following launches \n'
    message_constructed += message

    #Send a message
    to_email = content[2]
    server.sendmail(from_email, to_email, message_constructed)
    print(message_constructed)
    
    server.quit()

    

def main():
##    base_url = 'https://launchlibrary.net/1.1/launch'
##    rocket_family = 'Falcon'
##    number_of_pages = rocket_launches.get_number_of_pages(base_url, rocket_family)
##    rocket_launches.get_list_of_launches(base_url, rocket_family, number_of_pages)
##
##    rocket_families_list = rocket_launches.get_list_of_rocket_families()
##    
##    rocket_launches.number_of_launches_per_family(rocket_families_list)

    launches_tomorrow_message =  rocket_launches.launches_tomorrow()
    send_email(launches_tomorrow_message)
    
main()
