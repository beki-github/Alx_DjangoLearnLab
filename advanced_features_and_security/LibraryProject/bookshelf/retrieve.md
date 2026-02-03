# Retrieve Operation

## Command:
```python
from bookshelf.models import Book

# Retrieve the book we created
book = Book.objects.get(title="1984")

print(f"Title: {book.title}")
print(f"Author: {book.author}")
print(f"Publication Year: {book.publication_year}")
```

## Output:
```text
Title: 1984
Author: George Orwell
Publication Year: 1949
```
