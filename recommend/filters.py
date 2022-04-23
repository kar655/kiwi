from typing import List
import datetime

class Filters:

    @staticmethod
    def by_date(events, date_range):
        return events # TODO implement

    @staticmethod
    def by_keywords(events, keywords):
        def contains_any_keyword(evt):
            texts = [evt.name, evt.description]
            texts = map(str.lower, texts)
            words = sum(map(str.split, texts), [])
            return any(kw.lower() in words for kw in keywords)

        return list(filter(contains_any_keyword, events))
