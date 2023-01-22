import pytest
from main import BooksCollector
@pytest.fixture
def collector():
    return BooksCollector()
def test_add_new_book(collector):
    collector.add_new_book("Harry Potter")
    assert collector.get_book_rating("Harry Potter") == 1

def test_set_book_rating(collector):
    collector.add_new_book("Harry Potter")
    collector.set_book_rating("Harry Potter", 8)
    assert collector.get_book_rating("Harry Potter") == 8

def test_get_books_with_specific_rating(collector):
    collector.add_new_book("Harry Potter")
    collector.set_book_rating("Harry Potter", 8)
    collector.add_new_book("The Lord of the Rings")
    collector.set_book_rating("The Lord of the Rings", 8)
    collector.add_new_book("The Hobbit")
    collector.set_book_rating("The Hobbit", 9)
    assert collector.get_books_with_specific_rating(8) == ["Harry Potter", "The Lord of the Rings"]

def test_add_book_in_favorites(collector):
    collector.add_new_book("Harry Potter")
    collector.add_book_in_favorites("Harry Potter")
    assert "Harry Potter" in collector.get_list_of_favorites_books()

def test_delete_book_from_favorites(collector):
    collector.add_new_book("Harry Potter")
    collector.add_book_in_favorites("Harry Potter")
    collector.delete_book_from_favorites("Harry Potter")
    assert "Harry Potter" not in collector.get_list_of_favorites_books()
