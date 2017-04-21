from icalendar import Calendar, Event

import urllib3


def cal_test():

    http = urllib3.PoolManager()
    r = http.request('GET', 'https://ntnu.blackboard.com/webapps/calendar/calendarFeed/d93aee49380f4c3ca9268f8a16dd92ae/learn.ics')

    cal = Calendar.from_ical(r.data)

    for event in cal.walk('vevent'):

        uid = str(event.get('uid'))


        summery = event.get('summary')
        print(str(summery))

        start = event.get('dtstart')
        print(start.dt)

        end = event.get('dtend')
        print(end.dt)

        description = event.get('description')
        print(str(description))

        print("\n")




    return


cal_test()
