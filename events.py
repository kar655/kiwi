from eventbrite import Eventbrite


class Events:
    def __init__(self, api_key):
        self.eventbrite = Eventbrite(api_key)

    def get_event_list(self, event_ids):
        return [self.eventbrite.get_event(e_id) for e_id in event_ids]
                