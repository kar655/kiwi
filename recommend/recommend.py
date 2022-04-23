from typing import List

from events import Event
from recommend.filters import Filters


def give_recommendations(events: List[Event], search_keywords : List[str], date_range) -> List[Event]:
    # Top-level function to be used to generate recommendations.

    # Other arguments are constraints to the filtering engine.
    events = Filters.by_date(events, date_range)
    events = Filters.by_keywords(events, search_keywords)
    return events


