from dataclasses import dataclass
import json
from typing import List


class Event:
    def __init__(self, data):
        self.id = self.trycall(lambda: data['id'])
        self.name = self.trycall(lambda: data['name']['text'])
        self.description = self.trycall(lambda: data['description']['text'])
        self.datetime = self.trycall(lambda: data['start']['utc'])

    def trycall(self, func):
        try:
            return func()
        except Exception as e:
            return None

    def __str__(self):
        return f'Event(name={self.name}, description={self.description}, datetime={self.datetime})'

    def __repr__(self):
        return self.__str__()


class EventsManager:
    def __init__(self):
        pass

    def get_event_list(self, event_ids: List[str]) -> List[Event]:
        return [self.eventbrite.get_event(e_id) for e_id in event_ids]

    def get_all_events(self) -> List[Event]:
        with open('data/data.json') as file:
            raw_events = json.load(file)
            return [Event(event) for event in raw_events]
