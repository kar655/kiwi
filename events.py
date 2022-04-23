from eventbrite import Eventbrite


class Events:
    def __init__(self, api_key):
        self.eventbrite = Eventbrite(api_key)
