from rest_framework import generics
from .models import Book
from .serializers import BookSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated

from django_filters import rest_framework
from rest_framework import filters

# ListView: Retrieve all books
# Allows read-only access for unauthenticated users, but restricts modification.
# Supports filtering, searching, and ordering.
class ListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [rest_framework.DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['title', 'author', 'publication_year']
    search_fields = ['title', 'author__name']
    ordering_fields = ['title', 'publication_year']

# DetailView: Retrieve a single book by ID
# Allows read-only access for unauthenticated users.
class DetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# CreateView: Add a new book
# Restricted to authenticated users only.
class CreateView(generics.CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    # Custom behavior: Ensure validation logic is handled in the serializer (already implemented)
    def perform_create(self, serializer):
        # We can add custom logic here if needed, for now standard save is sufficient
        serializer.save()

# UpdateView: Modify an existing book
# Restricted to authenticated users only.
class UpdateView(generics.UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    # Custom behavior: Example of restricting updates (if requirements evolved)
    def perform_update(self, serializer):
        serializer.save()

# DeleteView: Remove a book
# Restricted to authenticated users only.
class DeleteView(generics.DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]
