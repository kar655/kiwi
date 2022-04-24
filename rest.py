from asyncio import events
from events import EventsManager
from flask import Flask, request, jsonify

import numpy as np
from events import EventsManager

from recommend.bert import Bert
from recommend.tokenize import clean_sentence

app = Flask(__name__)

all_events = EventsManager().get_all_events()

def prepare_model():
    events = all_events
    names = np.array([clean_sentence(evt.name + " " + evt.description) for evt in events])
    bert = Bert()
    names_encoded = bert.encode(names)
    return names_encoded, bert


names_encoded, bert = prepare_model()


all_events = EventsManager().get_all_events()

def event_data(evt):
        return {
            'id': evt.id,
            'name': evt.name,
            'description': evt.description,
            'picture': evt.img_url,
        }


@app.route("/event/<int:eid>")
def get_event(eid):
    evts = list(filter(lambda e: e.id == eid, all_events))
    return jsonify(event_data(evts[0]))

@app.route("/recommend/", methods=['POST'])
def recommend():
    data = request.get_json()
    
    search_data = data['search_data']
    user_data = data['user_data']
    username = user_data['name']
    preferences = user_data['preferences']
    user_events = user_data['events']

    predictions = bert.top_predictions(search_data, names_encoded)
    events = [e for i, e in enumerate(all_events) if i in predictions]
    # events = get_recommendations(all_events, str.split(search_data) + str.split(preferences))

    return jsonify({score: event_data(evt) for score, evt in enumerate(events)})

#  curl -d '{"search_data": "car", "user_data":{"name":"Macius", "preferences":"horse", "events":""}}' -H "Content-Type: application/json" -X POST http://localhost:5000/recommend/

if __name__ == '__main__':
    app.run(host='0.0.0.0')