from django.db import models

# The Author model represents a writer of books.
class Author(models.Model):
    name = models.CharField(max_length=200)  # The name of the author

    def __str__(self):
        return self.name

# The Book model represents a book written by an author.
class Book(models.Model):
    title = models.CharField(max_length=200)  # The title of the book
    publication_year = models.IntegerField()  # The year the book was published
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)  # Link to the Author model

    def __str__(self):
        return self.title
