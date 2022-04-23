from events import Events
from pprint import pprint


def main():
    api_key = 'A6FCWAHLHYF6EKU5HF2W'
    events = Events(api_key)
    pprint(events.eventbrite.get_user())


if __name__ == '__main__':
    main()
