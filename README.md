# Game Backend (Django REST API)

Simple REST backend to track games, players, per-player progress, and achievements. Designed to be used by game clients (web/mobile/desktop) or an admin UI.

## Features
- User registration and JWT authentication
- Game catalog (create/read/update/delete)
- Per-player progress (score, level)
- Achievements (global per game) and player achievement records
- Public leaderboard per game
- Django admin for content management
- API browsable in dev for quick manual testing

## Quick architecture summary
- Django + Django REST Framework
- JWT auth via djangorestframework-simplejwt
- Models:
  - Game: game metadata (name, description)
  - PlayerProgress: player, game, score, level (one per player+game)
  - Achievement: achievement tied to a game
  - PlayerAchievement: player unlocked achievement with timestamp

## Setup (Windows, PowerShell)
1. Open project folder:
   cd "C:\Users\hp\Desktop\Game dev\django\backened"
2. Activate venv:
   \venv\Scripts\Activate
3. Install deps:
   pip install -r requirements.txt
4. Apply migrations:
   python manage.py migrate
5. Create superuser:
   python manage.py createsuperuser
6. Run server:
   python manage.py runserver

Admin UI: http://127.0.0.1:8000/admin/

## Authentication
- Obtain token:
  POST /api/login/ with JSON { "username": "...", "password": "..." } → returns access + refresh tokens.
- Refresh token:
  POST /api/refresh/ with JSON { "refresh": "..." }.
- Use header for protected endpoints:
  Authorization: Bearer <access_token>

## Key API endpoints (router-based)
- POST /api/register/ — create user.
- POST /api/login/ — get JWT tokens.
- GET /api/me/ — current user (authenticated).
- /api/games/ (ModelViewSet) — list/retrieve/create/update/delete games.
  - Note: creation/edit/delete are admin-only via API.
  - GET /api/games/<id>/leaderboard/ — public leaderboard for a game.
- /api/playerprogress/ — authenticated users create/update their game progress.
- /api/achievements/ — admin can manage achievements.
- POST /api/achievements/<id>/unlock/ (or provided unlock endpoint) — authenticated user unlocks an achievement.
- GET /api/my-achievements/ — authenticated user's achievements.

(Use the browsable API or inspect core/urls.py for exact route names if needed.)

## Who can add games
- By default this project requires an admin user to create/edit/delete games via the API (GameViewSet uses IsAdminUser).
- Admins can also add games in the Django admin UI.

## Create admin and add a game (short)
1. Create admin:
   python manage.py createsuperuser
2. Login to admin at /admin/ and add a Game, or:
3. Via API (Thunder Client / curl):
   - POST /api/login/ → get access token
   - POST /api/games/ with header Authorization: Bearer <token> and body:
     { "name": "My Game", "description": "..." }

## Example Thunder Client requests
1. Login (POST)
   URL: http://127.0.0.1:8000/api/login/
   Body JSON: { "username": "admin", "password": "..." }

2. Create game (POST)
   URL: http://127.0.0.1:8000/api/games/
   Headers: Authorization: Bearer <access_token>, Content-Type: application/json
   Body JSON: { "name": "New Game", "description": "Short desc" }

## Testing
- API tests exist in core/tests.py. Run:
  python manage.py test

## Recording a demo (browser)
- Start server, open two tabs: API root (/api/) and Admin (/admin/).
- Record clips: register, login, create progress, unlock achievement, show leaderboard, open admin and edit a game.
- Use a browser screen recorder (getDisplayMedia + MediaRecorder or an extension like Loom) and convert to MP4 if needed.

## Notes & customization
- Permission behavior is controlled in core/views.py (GameViewSet.permission_classes). Change to IsAuthenticated to allow any logged-in user to create games.
- CORS handled via django-cors-headers (ensure it's installed if enabled in settings).

## Files of interest
- core/models.py — data model
- core/views.py — endpoints and permissions
- core/serializers.py — payload validation/representation
- core/admin.py — admin UI config
- game_backend/settings.py — global settings (REST_FRAMEWORK, SIMPLE_JWT, CORS)
- core/urls.py & game_backend/urls.py — routing

