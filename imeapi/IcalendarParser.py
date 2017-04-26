from icalendar import Calendar, Event
import certifi
import urllib3


def icalendar_parser():
    """Laying the groundwork for future functionality, where events is parsed from the ical-feeds from Its Learning and
    Blackboard. Not an feature complete file, and is not used in production at the momement."""
    # opens a secure connection to the feed source
    http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
    r = http.request('GET', 'https://ntnu.itslearning.com/Calendar/CalendarFeed.ashx?LocationType=3&LocationID=0&PersonId=122979&CustomerId=105&ChildId=0&Guid=5c602cad73b1dfce22dcb64372f18e17&Culture=nb-NO&FavoriteOnly=True')

    cal = Calendar.from_ical(r.data)

    for event in cal.walk('vevent'):

        uid = str(event.get('uid'))

        summary = event.get('summary')
        start = event.get('dtstart')
        end = event.get('dtend')
        description = event.get('description')
