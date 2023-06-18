from database import Base
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.sql import text
from sqlalchemy import Column, Integer, String, Boolean


class User(Base):
    __tablename__ = 'users'

    uuid = Column(UUID(as_uuid=True), primary_key=True, server_default=text("(uuid_generate_v4())"))
    telegram_id = Column(Integer)
    is_bot = Column(Boolean)
    first_name = Column(String)
    last_name = Column(String)
    username = Column(String)
    language_code = Column(String, nullable=True)

    def __repr__(self):
        return f"User(telegram_id={self.telegram_id}, is_bot={self.is_bot}, first_name='{self.first_name}', last_name='{self.last_name}', username='{self.username}', language_code='{self.language_code}')"

    def __init__(self, user_data):
        self.telegram_id = user_data['id']
        self.is_bot = user_data['is_bot']
        self.first_name = user_data['first_name']
        self.last_name = user_data['last_name']
        self.username = user_data['username']
        self.language_code = user_data.get('language_code')