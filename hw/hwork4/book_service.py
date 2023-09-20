from book_repository import BookRepository


class BookService:
    def __init__(self, repository):
        self.repository = repository

    def get_book_title(self, book_id):
        book = self.repository.get_book_by_id(book_id)
        return book['title']


repository = BookRepository()

book_service = BookService(repository)

title = book_service.get_book_title(1)
print(title)
