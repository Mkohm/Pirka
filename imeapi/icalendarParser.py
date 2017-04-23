from icalendar import Calendar, Event
import certifi

import urllib3


def icalendar_parser():

    # opens a secure connection to the feed source
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    r = http.request('GET', 'https://ntnu.itslearning.com/Calendar/CalendarFeed.ashx?LocationType=3&LocationID=0&PersonId=122979&CustomerId=105&ChildId=0&Guid=5c602cad73b1dfce22dcb64372f18e17&Culture=nb-NO&FavoriteOnly=True')

    cal = Calendar.from_ical(r.data)

    for event in cal.walk('vevent'):

        uid = str(event.get('uid'))

        summary = event.get('summary')
        print(str(summary))

        start = event.get('dtstart')
        print(start.dt)

        end = event.get('dtend')
        print(end.dt)

        description = event.get('description')
        print(str(description))

        print("\n")

icalendar_parser()
