import unittest
from unittest.mock import Mock
from home_work.solid_task import LibraryManager


class TestLibraryManager(unittest.TestCase):
    def setUp(self):
        self.mock_library = Mock()
        self.manager = LibraryManager(self.mock_library)

    def test_add_book_valid_year(self):
        self.manager.add_book("1984", "George Orwell", "1949")
        self.mock_library.add_book.assert_called_once()
        added_book = self.mock_library.add_book.call_args[0][0]
        self.assertEqual(added_book.title, "1984")
        self.assertEqual(added_book.author, "George Orwell")
        self.assertEqual(added_book.year, "1949")

    def test_add_book_invalid_year(self):
        self.manager.add_book(
            "The Hobbit", "J.R.R. Tolkien", "Nineteen Thirty-Seven")
        self.mock_library.add_book.assert_called_once()

    def test_remove_book(self):
        self.manager.remove_book("Moby Dick")
        self.mock_library.remove_book.assert_called_once_with("Moby Dick")

    def test_show_books(self):
        self.manager.show_books()
        self.mock_library.show_books.assert_called_once()


if __name__ == "__main__":
    unittest.main()
