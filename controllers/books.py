from fastapi import APIRouter, Depends, HTTPException, status
from models.book import BookCreate, BookUpdate, BookInDB
from repositories.book_repository import BookRepository
from .auth import get_current_user, get_current_author
from models.user import User

router = APIRouter(prefix="/api/v1/books", tags=["books"])
book_repo = BookRepository()

@router.get("", response_model=list[BookInDB])
async def read_books():
    return book_repo.get_all_books()

@router.get("/{book_id}", response_model=BookInDB)
async def read_book(book_id: int, current_user: User = Depends(get_current_user)):
    book = book_repo.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    return book

@router.post("", response_model=BookInDB)
async def create_book(
    book: BookCreate,
    current_user: User = Depends(get_current_author)
):
    return book_repo.create_book(book, current_user.id)

@router.patch("/{book_id}", response_model=BookInDB)
async def update_book(
    book_id: int,
    book_update: BookUpdate,
    current_user: User = Depends(get_current_author)
):
    book = book_repo.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    if book.author_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only update your own books"
        )
    return book_repo.update_book(book_id, book_update.dict(exclude_unset=True))

@router.delete("/{book_id}")
async def delete_book(
    book_id: int,
    current_user: User = Depends(get_current_author)
):
    book = book_repo.get_book_by_id(book_id)
    if not book:
        raise HTTPException(status_code=404, detail="Book not found")
    if book.author_id != current_user.id:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You can only delete your own books"
        )
    book_repo.delete_book(book_id)
    return {"message": "Book deleted successfully"}