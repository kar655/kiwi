from dataclasses import dataclass
import json
from typing import List
from dacite import from_dict

class Event:
    def __init__(self, data):
        self.name = self.trycall(lambda _: data['name']['text'])
        self.description = self.trycall(lambda _: data['description']['text'])
        self.datetime = self.trycall(lambda _: data['start']['utc'])

    def trycall(self, func):
        try:
            return func()
        except Exception as e:
            return None

# @dataclass
# class Event:
#     @dataclass
#     class TextHtml:
#         text: str
#         html: str

#     name: TextHtml
#     description: TextHtml

#     @dataclass
#     class Timestamp:
#         timezone: str
#         local: str
#         utc: str
#     start: Timestamp
#     end: Timestamp
    

class EventsManager:
    def __init__(self):
        pass

    def get_event_list(self, event_ids: List[str]) -> List[Event]:
        return [self.eventbrite.get_event(e_id) for e_id in event_ids]
                
    def get_all_events(self) -> List[Event]:
        with open('data/data.json') as file:
            raw_events = json.load(file)
            return [Event(event) for event in raw_events] # TODO just temporary
            # return [from_dict(data_class=Event, data=event) for event in raw_events]
