from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author
from django.urls import reverse

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username='testuser', password='password')
        
        # Create an author
        self.author = Author.objects.create(name="Test Author")
        
        # Create a book
        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2023,
            author=self.author
        )
        
        # URLs
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', args=[self.book.id])
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', args=[self.book.id])
        self.delete_url = reverse('book-delete', args=[self.book.id])

    def test_list_books_unauthenticated(self):
        """Test that unauthenticated users can list books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that response.data is a list (assuming no pagination)
        self.assertIsInstance(response.data, list)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Test Book")

    def test_list_books_authenticated(self):
        """Test that authenticated users can list books."""
        self.client.login(username='testuser', password='password')
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_detail_book_unauthenticated(self):
        """Test that unauthenticated users can retrieve a book detail."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Test Book")

    def test_create_book_authenticated(self):
        """Test that authenticated users can create a book."""
        self.client.login(username='testuser', password='password')
        data = {
            'title': 'New Book',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)
        self.assertEqual(Book.objects.get(id=response.data['id']).title, 'New Book')

    def test_create_book_unauthenticated(self):
        """Test that unauthenticated users cannot create a book."""
        data = {
            'title': 'Unauthorized Book',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_book_authenticated(self):
        """Test that authenticated users can update a book."""
        self.client.login(username='testuser', password='password')
        data = {
            'title': 'Updated Book Title',
            'publication_year': 2023,
            'author': self.author.id
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, 'Updated Book Title')

    def test_update_book_unauthenticated(self):
        """Test that unauthenticated users cannot update a book."""
        data = {
            'title': 'Hacked Title',
            'publication_year': 2023,
            'author': self.author.id
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_authenticated(self):
        """Test that authenticated users can delete a book."""
        self.client.login(username='testuser', password='password')
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_delete_book_unauthenticated(self):
        """Test that unauthenticated users cannot delete a book."""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(Book.objects.count(), 1)

    def test_filter_books_by_author(self):
        """Test filtering books by author."""
        new_author = Author.objects.create(name="Another Author")
        Book.objects.create(title="Another Book", publication_year=2022, author=new_author)
        
        response = self.client.get(self.list_url, {'author': self.author.id})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Assuming pagination, results are in 'results' or direct list if no pagination
        # Check structure
        results = response.data.get('results', response.data) if isinstance(response.data, dict) else response.data
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['author'], self.author.id)

    def test_search_books(self):
        """Test searching books by title."""
        Book.objects.create(title="Django Advanced", publication_year=2022, author=self.author)
        
        response = self.client.get(self.list_url, {'search': 'Django'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data.get('results', response.data) if isinstance(response.data, dict) else response.data
        self.assertEqual(len(results), 1)
        self.assertEqual(results[0]['title'], "Django Advanced")

    def test_ordering_books(self):
        """Test ordering books by publication year."""
        Book.objects.create(title="Old Book", publication_year=2020, author=self.author)
        
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        results = response.data.get('results', response.data) if isinstance(response.data, dict) else response.data
        self.assertEqual(results[0]['publication_year'], 2020)
        self.assertEqual(results[-1]['publication_year'], 2023)
