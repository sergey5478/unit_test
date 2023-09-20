import unittest
from unittest.mock import patch

from book_service import BookService
from book_repository import BookRepository


class TestBook(unittest.TestCase):
    @patch('book_repository.BookRepository')
    def test_get_book_title(self, mock_repository):
        mock_repository_instance = mock_repository.return_value
        mock_repository_instance.get_book_by_id.return_value = {'id': 1, 'title': 'Sample Book'}

        book_service = BookService(mock_repository_instance)

        title = book_service.get_book_title(1)

        mock_repository_instance.get_book_by_id.assert_called_once_with(1)

        self.assertEqual(title, 'Sample Book')


if __name__ == '__main__':
    unittest.main()
