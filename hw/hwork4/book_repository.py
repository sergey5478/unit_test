class BookRepository:
    def __init__(self):
        self.books = {
            1: {'id': 1, 'title': 'Sample Book 1'},
            2: {'id': 2, 'title': 'Sample Book 2'},
        }

    def get_book_by_id(self, book_id):
        return self.books.get(book_id)
