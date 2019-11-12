import ticketpy
from tok import secret
import pprint

token = secret()
tm_client = ticketpy.ApiClient(token)
pp = pprint.PrettyPrinter(indent=4)

def tm_api():
    # dictionary keys of argument are the fields we care about
    argument = {'city': 'Austin', 'startDateTime': '2014-03-31T19:15:00Z',
    'keyword': 'Sports', 'radius': '50'}

    # do something like this...
    # argument["city"] =

    pages = tm_client.events.find(**argument)

    list_of_events = []

    for page in pages:
        for event in page:
            #populate this dictionary with info from the search
            if ("name" in event.json and "url" in event.json and
            "localTime" in event.json["dates"]["start"]
            and event.json["images"][0] and "address" in event.json["_embedded"]["venues"][0] and
            "name" in event.json["_embedded"]["venues"][0]):
                dict = {}
                dict["name"] = event.json["name"]
                dict["url"] = event.json["url"]
                dict["date"] = event.json["dates"]["start"]["localTime"]
                dict["image"] = event.json["images"][0]
                dict["address"] = event.json["_embedded"]["venues"][0]["address"]
                dict["venue_name"] = event.json["_embedded"]["venues"][0]["name"]
                pp.pprint(dict)
                list_of_events.append(dict)

tm_api()
