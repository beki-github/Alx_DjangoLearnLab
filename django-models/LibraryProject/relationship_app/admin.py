from django.contrib import admin
from .models import Author, Book, Library, Librarian

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'book_count')
    
    def book_count(self, obj):
        return obj.books.count()
    book_count.short_description = 'Number of Books'

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'library_count')
    list_filter = ('author',)
    search_fields = ('title', 'author__name')
    
    def library_count(self, obj):
        return obj.libraries.count()
    library_count.short_description = 'Available in Libraries'

@admin.register(Library)
class LibraryAdmin(admin.ModelAdmin):
    list_display = ('name', 'book_count', 'has_librarian')
    
    def book_count(self, obj):
        return obj.books.count()
    book_count.short_description = 'Number of Books'
    
    def has_librarian(self, obj):
        return hasattr(obj, 'librarian')
    has_librarian.boolean = True

@admin.register(Librarian)
class LibrarianAdmin(admin.ModelAdmin):
    list_display = ('name', 'library')
