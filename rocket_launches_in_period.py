import requests as r
import datetime as d


def launches_in_period(today_date=d.date.today(), future_date=d.date.today() + d.timedelta(days=3)):
    upcoming_launches = r.get('https://launchlibrary.net/1.2/launch/{0}/{1}'.format(today_date, future_date))
    upcoming_launches_dict = upcoming_launches.json()
    if upcoming_launches_dict['count'] > 0:
        upcoming_launches_number = upcoming_launches_dict['count']
        launch_list = []
        for i in range(0, upcoming_launches_number):
            launch_dict = {}
            launch_dict['launch_name'] = upcoming_launches_dict['launches'][i]['name']
            launch_dict['net'] = upcoming_launches_dict['launches'][i]['net']
            if not upcoming_launches_dict['launches'][i]['vidURLs']:
                launch_dict['vidURLs'] = "No video coverage."
            else:
                launch_dict['vidURLs'] = upcoming_launches_dict['launches'][i]['vidURLs'][0]
            launch_dict['location_name'] = upcoming_launches_dict['launches'][i]['location']['pads'][0]['name']
            launch_dict['rocket_name'] = upcoming_launches_dict['launches'][i]['rocket']['name']
            if not upcoming_launches_dict['launches'][i]['missions']:
                launch_dict['mission_description'] = "No further description."
            else:
                launch_dict['mission_description'] = upcoming_launches_dict['launches'][i]['missions'][0]['description']
            launch_list.append(launch_dict)
        return launch_list
    else:
        # Message for no launches
        list_of_upcoming_launches = ['No upcoming launches']
        return list_of_upcoming_launches


def compose_message_for_upcoming_launches(list_of_upcoming_launches):
    message_constructed = ""
    if list_of_upcoming_launches[0] != 'No upcoming launches':
        for launch, launch_info in enumerate(list_of_upcoming_launches):
            message_constructed += "Name: " + list_of_upcoming_launches[launch]['launch_name'] + "\n"
            message_constructed += "Launch NET: " + list_of_upcoming_launches[launch]['net'] + "\n"
            message_constructed += "Link for video: " + list_of_upcoming_launches[launch]['vidURLs'] + "\n"
            message_constructed += "Launching from: " + list_of_upcoming_launches[launch]['location_name'] + "\n"
            message_constructed += "Launch vehicle: " + list_of_upcoming_launches[launch]['rocket_name'] + "\n"
            message_constructed += "Mission description: " \
                                   + list_of_upcoming_launches[launch]['mission_description'] + "\n" + "\n"
    return message_constructed


def verify_launches_will_happen(today_date=d.date.today(), future_date=d.date.today() + d.timedelta(days=3)):
    upcoming_launches = r.get('https://launchlibrary.net/1.2/launch/{0}/{1}'.format(today_date, future_date))
    upcoming_launches_dict = upcoming_launches.json()
    if upcoming_launches_dict['count'] > 0:
        return True
    else:
        return False
