import datetime


def datetimearray():
    current = datetime.datetime.now()  # https://www.w3schools.com/python/python_datetime.asp
    log = [str(current.date()), str(current.strftime("%X"))]
    return log
