# kiwi
The repo contains backend part of the project.
It provides ML-based event recommendation system.

Install requirements and run server using `python rest.py`

Exemplary request
```curl -d '{"search_data": "programming", "user_data":{"name":"Matt", "preferences":"horse", "events":""}}' -H "Content-Type: application/json" -X POST http://localhost:5000/recommend/```
