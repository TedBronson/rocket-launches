import requests as r
import math


def get_list_of_launches(base_url, rocket_family, number_of_pages):
    for current_page in range(number_of_pages):
        current_page = current_page * 10

        request_url = base_url
        request_url += '?name=' + rocket_family
        request_url += '&offset=' + str(current_page)

        launches = r.get(request_url)
        launches_json = launches.json()
        total = launches_json['total']
        for launch in launches_json['launches']:
            date = launch['net']
            print(date)

    print('Total number of launches seen is: ' + str(total))


def get_number_of_pages(base_url, rocket_family):
    launches = r.get(base_url + '?name=' + rocket_family)
    launches_json = launches.json()
    number_of_pages = int(launches_json['total']) / int(launches_json['count'])
    number_of_pages = math.ceil(number_of_pages)
    number_of_pages = number_of_pages

    return number_of_pages


def get_list_of_rocket_families():
    rocket_families = r.get('https://launchlibrary.net/1.1/rocketfamily')
    rocket_families_json = rocket_families.json()
    rocket_families_list = []
    for rocket_family_object in rocket_families_json['RocketFamilies']:
        rocket_family = rocket_family_object['name']
        rocket_families_list.append(rocket_family)

    return rocket_families_list


def number_of_launches_per_family(rocket_families_list):
    for rocket_family in rocket_families_list:
        launches_of_family = r.get('https://launchlibrary.net/1.1/launch' + '?name=' + rocket_family)
        launches_of_family_json = launches_of_family.json()
        if launches_of_family_json['count'] == 0:
            print(rocket_family + ' was never launched.')
            continue

        number_of_launches = launches_of_family_json['total']
        print(rocket_family + ' was launched: ' + str(number_of_launches) + ' times')


def main():
    base_url = 'https://launchlibrary.net/1.1/launch'
    rocket_family = 'Falcon'
    # number_of_pages = get_number_of_pages(base_url, rocket_family)
    # get_list_of_launches(base_url, rocket_family, number_of_pages)

    rocket_families_list = get_list_of_rocket_families()

    number_of_launches_per_family(rocket_families_list)


main()
