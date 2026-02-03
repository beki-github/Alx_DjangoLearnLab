# Delete Operation

## Command:
```python
from bookshelf.models import Book

# Get the book to delete
book = Book.objects.get(title="Nineteen Eighty-Four")

# Delete the book
book.delete()

# Verify deletion
remaining_books = Book.objects.all()
print(f"Books remaining: {remaining_books.count()}")
```

## Output:
```text
Books remaining: 0
```
