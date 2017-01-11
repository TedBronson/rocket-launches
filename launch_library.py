from rocket_launches_in_period import launches_in_period,\
    compose_message_for_upcoming_launches,\
    verify_launches_will_happen

from emailer import send_email


def main():
    # if rocket_launches_in_period.verify_launches_will_happen():
    launches_tomorrow_message = compose_message_for_upcoming_launches(launches_in_period())
    send_email(launches_tomorrow_message)

main()
