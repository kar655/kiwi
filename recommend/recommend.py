from typing import List

class Event:
    pass # TODO


def give_recommendations(events : List[Event], search_keywords : List[str], date_range) -> List[Event]:
    # Top-level function to be used to generate recommendations.

    # Other arguments are constraints to the filtering engine.
    events = Filter.by_date(event_database, date_range)
    events = Filter.by_keywords(events, search_keywords)
    return events


class Filter:

    @staticmethod
    def by_date(events, date_range):
        pass

    def by_keywords(events, keywords):
        pass