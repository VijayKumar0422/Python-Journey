import datetime


def current_time():

    now = datetime.datetime.now()

    return now.strftime("Current Time : %I:%M:%S %p")


def current_date():

    today = datetime.datetime.now()

    return today.strftime("Current Date : %d-%m-%Y")