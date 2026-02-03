#!/usr/bin/env python
"""Sample queries demonstrating model relationships"""

import os
import django
import sys

# Setup Django
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from relationship_app.models import Author, Book, Library, Librarian

def query_all_books_by_author(author_name):
    """Query 1: Get all books by a specific author"""
    try:
        author = Author.objects.get(name=author_name)
        books = Book.objects.filter(author=author)
        print(f"\n1. All books by {author_name}:")
        for book in books:
            print(f"   - {book.title}")
        return books
    except Author.DoesNotExist:
        print(f"Author '{author_name}' not found")
        return []

def list_all_books_in_library(library_name):
    """Query 2: List all books in a specific library"""
    try:
        library = Library.objects.get(name=library_name)
        books = library.books.all()
        print(f"\n2. All books in '{library_name}' library:")
        for book in books:
            print(f"   - {book.title} by {book.author.name}")
        return books
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found")
        return []

def retrieve_librarian_for_library(library_name):
    """Query 3: Get the librarian for a specific library"""
    try:
        library = Library.objects.get(name=library_name)
        librarian = Librarian.objects.get(library=library)
        print(f"\n3. Librarian for '{library_name}':")
        print(f"   - {librarian.name}")
        return librarian
    except Library.DoesNotExist:
        print(f"Library '{library_name}' not found")
        return None
    except Librarian.DoesNotExist:
        print(f"No librarian found for '{library_name}'")
        return None

def demonstrate_relationships():
    """Demonstrate all relationship queries"""
    print("=" * 50)
    print("DEMONSTRATING DJANGO MODEL RELATIONSHIPS")
    print("=" * 50)
    
    # Query 1: ForeignKey relationship
    query_all_books_by_author("George Orwell")
    
    # Query 2: ManyToMany relationship  
    list_all_books_in_library("Main City Library")
    
    # Query 3: OneToOne relationship
    retrieve_librarian_for_library("Main City Library")
    
    print("\n" + "=" * 50)
    print("ADDITIONAL RELATIONSHIP DEMONSTRATIONS")
    print("=" * 50)
    
    # Reverse ForeignKey lookup
    print("\n4. Reverse ForeignKey: Authors and their books")
    authors = Author.objects.all()
    for author in authors:
        book_count = author.books.count()
        print(f"   - {author.name}: {book_count} books")
    
    # ManyToMany reverse lookup
    print("\n5. ManyToMany Reverse: Books and their libraries")
    books = Book.objects.all()[:3]  # First 3 books
    for book in books:
        libraries = book.libraries.all()
        lib_names = [lib.name for lib in libraries]
        print(f"   - {book.title}: available in {lib_names if lib_names else 'no libraries'}")
    
    # OneToOne reverse lookup
    print("\n6. OneToOne Reverse: Libraries and their librarians")
    libraries = Library.objects.all()
    for library in libraries:
        try:
            librarian = library.librarian
            print(f"   - {library.name}: {librarian.name}")
        except Librarian.DoesNotExist:
            print(f"   - {library.name}: No librarian assigned")

if __name__ == "__main__":
    # First, create sample data if needed (assuming user might run this standalone)
    # Using relative import workaround for direct execution
    try:
        from create_sample_data import create_sample_data
        print("Creating/Refreshing sample data...")
        create_sample_data()
    except ImportError:
        pass
    
    # Run demonstration
    demonstrate_relationships()
