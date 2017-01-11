import requests as r
import datetime as d


def launches_in_period(first_date=d.date.today(), second_date=d.date.today() + d.timedelta(days=10)):
    # Calculate delta in days
    delta = second_date - first_date
    delta = delta.days

    upcoming_launches = r.get('https://launchlibrary.net/1.2/launch/{0}/{1}'.format(first_date, second_date))
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
        return launch_list, delta
    else:
        # Message for no launches
        list_of_upcoming_launches = ['No upcoming launches']
        return (list_of_upcoming_launches, delta)


def compose_message_for_upcoming_launches((list_of_upcoming_launches, delta)):
    message_constructed = ""
    if list_of_upcoming_launches[0] != 'No upcoming launches':
        for launch, launch_info in enumerate(list_of_upcoming_launches):
            launch_path = list_of_upcoming_launches[launch]
            message_constructed = "In next {6} days we are expecting following launches: \n \n" \
                                  "Name: {0} \n" \
                                  "Launch NET: {1} \n" \
                                  "Link for video: {2} \n" \
                                  "Launching from: {3} \n" \
                                  "Launch vehicle: {4} \n" \
                                  "Mission description: {5} \n \n".format(
                launch_path['launch_name'],
                launch_path['net'],
                launch_path['vidURLs'],
                launch_path['location_name'],
                launch_path['rocket_name'],
                launch_path['mission_description'],
                delta
            )

    return message_constructed


def verify_launches_will_happen(today_date=d.date.today(), future_date=d.date.today() + d.timedelta(days=3)):
    upcoming_launches = r.get('https://launchlibrary.net/1.2/launch/{0}/{1}'.format(today_date, future_date))
    upcoming_launches_dict = upcoming_launches.json()
    if upcoming_launches_dict['count'] > 0:
        return True
    else:
        return False
