from asyncio import events
from events import EventsManager
from flask import Flask, request, jsonify
from recommend.recommend import get_recommendations

app = Flask(__name__)

all_events = EventsManager().get_all_events()

@app.route("/recommend/", methods=['POST'])
def recommend():
    data = request.get_json()
    keywords = data['keywords']
    events = get_recommendations(all_events, keywords, None)

    return jsonify({evt.id : evt.name for evt in events})