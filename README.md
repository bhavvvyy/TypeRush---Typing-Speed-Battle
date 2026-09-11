# Typing Speed Battle by TriDev

A futuristic typing-speed game with AI opponent, DSA-based scoring, a Django backend, REST API, SQLite database, and Render deployment support.

## Technology Used
- HTML, CSS and JavaScript – frontend and game interaction
- Python – backend programming
- Django – web framework and server-side logic
- Django REST Framework – RESTful API for typing results
- SQLite – database for leaderboard results
- GitHub – source control
- Render – deployment and hosting

## Main Features
- Typing speed test with Easy, Medium and Hard modes
- 30s / 60s / 120s game durations
- AI opponent
- WPM and accuracy tracking
- LCS Dynamic Programming for accuracy
- Sliding Window for live WPM
- Max Heap / Priority Queue for leaderboard ranking
- Backend leaderboard stored in SQLite
- REST API for creating, reading, updating and deleting results

## API Endpoints
- `GET /api/results/`
- `POST /api/results/`
- `GET /api/results/<id>/`
- `PUT /api/results/<id>/`
- `DELETE /api/results/<id>/`
- `DELETE /api/results/clear/`

## Run Locally
```bash
python -m venv venv
# Windows: venv\\Scripts\\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```
Then open `http://127.0.0.1:8000/`.

## DSA Used in the Game
- Longest Common Subsequence (Dynamic Programming) for accuracy calculation
- Sliding Window for real-time WPM calculation
- Max Heap / Priority Queue for leaderboard ranking
