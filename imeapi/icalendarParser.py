from icalendar import Calendar, Event
import certifi

import urllib3


def blackboard_parser():

    http = urllib3.PoolManager()
    r = http.request('GET', 'https://ntnu.blackboard.com/webapps/calendar/calendarFeed/7f902b41e0304ccd97426c82ce6df585/learn.ics')

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




    return


blackboard_parser()
