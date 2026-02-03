# Django Admin Interface Configuration

## 1. Admin Registration
Registered `Book` model in `bookshelf/admin.py`:

```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')
```

## 2. Features Configured
### List Display
- Title, Author, and Publication Year columns
- All fields visible at a glance

### Filtering
- Filter by Author
- Filter by Publication Year
- Right sidebar filters for quick navigation

### Search
- Search by Title
- Search by Author
- Real-time search functionality

## 3. Admin Access
- **URL**: http://127.0.0.1:8000/admin/
- **Login**: Use superuser credentials created with `python manage.py createsuperuser`
- **Navigation**: Bookshelf → Books

## 4. Expected Admin View
```text
+-----------------------------------------+
| Books (Admin)                           |
+-----------------------------------------+
| Add Book +        Search: [_______]     |
+-----------------------------------------+
| Title               | Author   | Year   |
+---------------------+----------+--------+
| 1984                | Orwell   | 1949   |
| To Kill a Mockingb..| Lee      | 1960   |
| The Great Gatsby    | Fitzgerald | 1925 |
+---------------------+----------+--------+
| Filters:                              |
| ✓ By Author          ▼                |
| ✓ By Year           ▼                 |
+--------------------------------------+
```
