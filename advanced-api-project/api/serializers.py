from rest_framework import serializers
from .models import Book, Author
import datetime

# The BookSerializer handles the serialization and validation of the Book model.
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    # Custom validation to ensure the publication year is not in the future.
    def validate_publication_year(self, value):
        current_year = datetime.date.today().year
        if value > current_year:
            raise serializers.ValidationError("Publication year cannot be in the future.")
        return value

# The AuthorSerializer handles the serialization of the Author model.
# It includes a nested BookSerializer to dynamically serialize related books.
class AuthorSerializer(serializers.ModelSerializer):
    # The books field is a nested serializer that serializes the related books for the author.
    # It is read-only to prevent modification of nested books directly through the author endpoint.
    books = BookSerializer(many=True, read_only=True)

    class Meta:
        model = Author
        fields = ['name', 'books']
