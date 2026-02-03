# Django Views and URL Configuration

## 1. Implemented Views

### Function-based View: `list_books`
**File:** `relationship_app/views.py`
```python
def list_books(request):
    books = Book.objects.all().select_related('author')
    return render(request, 'relationship_app/list_books.html', {'books': books})
```
**Template:** `list_books.html`
- Displays all books with titles and authors
- Shows total book count
- Styled with CSS

### Class-based Views
1. **LibraryListView** - Lists all libraries
```python
class LibraryListView(ListView):
    model = Library
    template_name = 'relationship_app/library_list.html'
```
2. **LibraryDetailView** - Shows library details with books
```python
class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
```

## 2. URL Configuration
**File:** `relationship_app/urls.py`
```python
urlpatterns = [
    path('books/', views.list_books, name='list_books'),
    path('libraries/', views.LibraryListView.as_view(), name='library_list'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library_detail'),
]
```

## 3. Templates Created
- `list_books.html`: Lists all books (function-based view)
- `library_list.html`: Lists all libraries (class-based view)
- `library_detail.html`: Shows library details (class-based view)

## 4. Testing URLs
- **Books List**: http://127.0.0.1:8000/books/
- **Libraries List**: http://127.0.0.1:8000/libraries/
- **Library Detail**: http://127.0.0.1:8000/library/1/
