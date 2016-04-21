import requests as r

def get_list_of_launches():
    launches = r.get('https://launchlibrary.net/1.1/launch')
    launches_json = launches.json()
    total = launches_json['total']
    for launch in launches_json['launches']:
        date = launch['net']
        print(date)

    print(total)

def main():
    get_list_of_launches()

    

main()
