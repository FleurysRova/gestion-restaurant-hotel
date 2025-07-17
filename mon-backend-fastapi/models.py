from sqlalchemy import Column, Integer, String
from databse import Base

class User(Base):
    __tablename__ = "users"

    user_id = Column(Integer, primary_key=True, index=True)
    user_name = Column(String(100))
    user_firstname = Column(String(100))
    user_email = Column(String(50), unique=True, index=True)
    user_phone = Column(Integer)
    user_adress = Column(String(50))
    user_password = Column(String(250))
