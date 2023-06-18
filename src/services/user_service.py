from database import db_session
from models.user import User


def create_user(user: User) -> User:
    print(f"Creating new user: {user}")
    db_session.add(user)
    db_session.commit()
    return user


def get_user_by_telegram_id(telegram_id: int) -> User:
    return User.query.filter(User.telegram_id == telegram_id).first()


def get_user(user_id: str) -> User:
    return User.query.get(user_id)


def get_all_users() -> list[User]:
    return User.query.all()


def update_user(user_id: str, name: str, language: str) -> User:
    user = User.query.get(user_id)
    if user:
        user.name = name
        user.language = language
        db_session.commit()
    return user


def delete_user(user_id: str) -> None:
    user = User.query.get(user_id)
    if user:
        db_session.delete(user)
        db_session.commit()
