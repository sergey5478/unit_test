class UserRepository:
    def get_user_by_id(self, user_id: int) -> str:
        return f'User {user_id}'
