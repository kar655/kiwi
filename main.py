from events import EventsManager
from pprint import pprint

from recommend.recommend import give_recommendations


def main():
    api_key = 'A6FCWAHLHYF6EKU5HF2W'
    events_manager = EventsManager()
    events = events_manager.get_all_events()
    
    events = give_recommendations(events, ['car', 'dance'], None)

    print(events[0])
    print(len(events))


if __name__ == '__main__':
    main()
