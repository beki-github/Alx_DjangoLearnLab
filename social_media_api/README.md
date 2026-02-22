# Social Media API

A robust Social Media API built with Django and Django REST Framework.

## Features
- Custom User Model with bio, profile picture, and following system.
- Token-based Authentication.
- User Registration and Login.
- User Profile management.
- Post Management (CRUD).
- Commenting system on posts.
- User following system (Follow/Unfollow).
- Dynamic activity feed showing posts from followed users.
- Liking and unliking system for posts.
- Real-time notifications for follows, likes, and comments.
- Search functionality for posts (by title and content).
- Pagination for posts and comments list views.

## Setup Instructions

### 1. Prerequisites
- Python 3.x
- pip

### 2. Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Alx_DjangoLearnLab/social_media_api
   ```

2. Install dependencies:
   ```bash
   pip install django djangorestframework
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Start the development server:
   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Authentication
- `POST /api/accounts/register/`: Register a new user. Returns a token.
- `POST /api/accounts/login/`: Log in an existing user. Returns a token.
- `GET/PUT/PATCH /api/accounts/profile/`: Retrieve or update the authenticated user's profile. (Requires Token Authentication)
- `POST /api/accounts/follow/<int:user_id>/`: Follow a user.
- `POST /api/accounts/unfollow/<int:user_id>/`: Unfollow a user.

### Posts & Comments
- `GET /api/posts/`: List all posts (Paginated, Searchable).
- `POST /api/posts/`: Create a new post.
- `GET/PUT/PATCH/DELETE /api/posts/<id>/`: Retrieve, update, or delete a specific post.
- `GET /api/posts/feed/`: View posts from people you follow.
- `POST /api/posts/<int:pk>/like/`: Like a post.
- `POST /api/posts/<int:pk>/unlike/`: Unlike a post.
- `GET /api/comments/`: List all comments (Paginated).
- `POST /api/comments/`: Create a new comment.
- `GET/PUT/PATCH/DELETE /api/comments/<id>/`: Retrieve, update, or delete a specific comment.

### Notifications
- `GET /api/notifications/`: Fetch all notifications for the authenticated user.

## Search and Filtering
- You can search posts by title or content using the `search` query parameter:
  `GET /api/posts/?search=keyword`

## Pagination
- Post and comment lists are paginated. You can navigate through pages using the `page` query parameter:
  `GET /api/posts/?page=2`

## User Model
The `CustomUser` model extends Django's `AbstractUser` and includes:
- `bio`: A text field for the user's biography.
- `profile_picture`: An image field for the user's profile picture.
- `followers`: A many-to-many field for the following system.
