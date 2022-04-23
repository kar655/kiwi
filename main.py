import numpy as np
from events import EventsManager
from pprint import pprint

from recommend.bert import Bert
from recommend.recommend import get_recommendations


def main():
    api_key = 'A6FCWAHLHYF6EKU5HF2W'
    events_manager = EventsManager()
    events = events_manager.get_all_events()

    names = np.array([evt.name for evt in events])

    bert = Bert()
    names_encoded = bert.encode(names)
    sentence = 'Programming'
    predictions = bert.top_predictions(sentence, names_encoded)
    names_predicted = names[predictions]
    pprint(names_predicted)

    # events = give_recommendations(events, ['car', 'dance'], None)

    # print(events[0])
    # print(len(events))


if __name__ == '__main__':
    main()
