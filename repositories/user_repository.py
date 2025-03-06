from models.user import UserInDB

class UserRepository:
    def __init__(self):
        self.users = {
            "author_user": UserInDB(
                id=1,
                username="author_user",
                password="authorpass",
                role="author"
            ),
            "reader_user": UserInDB(
                id=2,
                username="reader_user",
                password="readerpass",
                role="reader"
            ),
            "admin_user": UserInDB(
                id=3,
                username="admin_user",
                password="adminpass",
                role="admin"
            )
        }

    def get_user_by_username(self, username: str):
        return self.users.get(username)

    def authenticate_user(self, username: str, password: str):
        user = self.get_user_by_username(username)
        if not user or user.password != password:
            return None
        return user