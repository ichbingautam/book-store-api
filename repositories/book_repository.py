from models.book import BookInDB

class BookRepository:
    def __init__(self):
        self.books = []
        self.current_id = 1

    def get_all_books(self):
        return self.books.copy()

    def get_book_by_id(self, book_id: int):
        return next((b for b in self.books if b.id == book_id), None)

    def create_book(self, book_data, author_id: int):
        new_book = BookInDB(
            id=self.current_id,
            author_id=author_id,
            **book_data.dict()
        )
        self.books.append(new_book)
        self.current_id += 1
        return new_book

    def update_book(self, book_id: int, update_data: dict):
        book = self.get_book_by_id(book_id)
        if book:
            for key, value in update_data.items():
                setattr(book, key, value)
        return book

    def delete_book(self, book_id: int):
        self.books = [b for b in self.books if b.id != book_id]
        return True