#!/usr/bin/env python
"""Script to create sample data for relationship models"""

import os
import django
import sys

# Setup Django
# Add the project directory to sys.path to ensure modules can be found
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def create_sample_data():
    """Create sample authors, books, libraries, and librarians"""
    
    # Clear existing data
    Author.objects.all().delete()
    Book.objects.all().delete()
    Library.objects.all().delete()
    Librarian.objects.all().delete()
    
    # Create Authors
    authors = [
        Author(name="George Orwell"),
        Author(name="J.K. Rowling"),
        Author(name="J.R.R. Tolkien"),
        Author(name="Jane Austen"),
    ]
    Author.objects.bulk_create(authors)
    print("Created authors")
    
    # Create Books with ForeignKey to Authors
    orwell = Author.objects.get(name="George Orwell")
    rowling = Author.objects.get(name="J.K. Rowling")
    tolkien = Author.objects.get(name="J.R.R. Tolkien")
    austen = Author.objects.get(name="Jane Austen")
    
    books = [
        Book(title="1984", author=orwell),
        Book(title="Animal Farm", author=orwell),
        Book(title="Harry Potter and the Philosopher's Stone", author=rowling),
        Book(title="Harry Potter and the Chamber of Secrets", author=rowling),
        Book(title="The Hobbit", author=tolkien),
        Book(title="The Fellowship of the Ring", author=tolkien),
        Book(title="Pride and Prejudice", author=austen),
        Book(title="Sense and Sensibility", author=austen),
    ]
    Book.objects.bulk_create(books)
    print("Created books")
    
    # Create Libraries with ManyToMany to Books
    main_library = Library.objects.create(name="Main City Library")
    main_library.books.add(*Book.objects.filter(author=orwell))
    main_library.books.add(*Book.objects.filter(author=austen))
    
    fantasy_library = Library.objects.create(name="Fantasy Library")
    fantasy_library.books.add(*Book.objects.filter(author=rowling))
    fantasy_library.books.add(*Book.objects.filter(author=tolkien))
    
    print("Created libraries with books")
    
    # Create Librarians with OneToOne to Libraries
    Librarian.objects.create(name="Alice Johnson", library=main_library)
    Librarian.objects.create(name="Bob Smith", library=fantasy_library)
    
    print("Created librarians")
    print("\nSample data created successfully!")

if __name__ == "__main__":
    create_sample_data()
