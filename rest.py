from asyncio import events
from events import EventsManager
from flask import Flask, request, jsonify
from recommend.recommend import get_recommendations

app = Flask(__name__)

all_events = EventsManager().get_all_events()

@app.route("/recommend/", methods=['POST'])
def recommend():
    data = request.get_json()
    
    search_data = data['search_data']
    user_data = data['user_data']
    username = user_data['name']
    preferences = user_data['preferences']
    user_events = user_data['events']

    events = get_recommendations(all_events, str.split(search_data) + str.split(preferences))

    def event_data(evt):
        return {
            'id': evt.id,
            'name': evt.name,
            'description': evt.description,
        }

    return jsonify({score: event_data(evt) for score, evt in enumerate(events)})

#  curl -d '{"search_data": "car", "user_data":{"name":"Macius", "preferences":"horse", "events":""}}' -H "Content-Type: application/json" -X POST http://localhost:5000/recommend/