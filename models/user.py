from sqlalchemy import Column, Date, DateTime, Integer, String

from models import Base


class User(Base):
    __tablename__ = "user"

    id = Column(Integer, primary_key=True)
    status = Column(String)
    email = Column(String, index=True, unique=True)
    name = Column(String)
    birthday = Column(Date)
    creation_date = Column(DateTime)
    update_date = Column(DateTime)

    def __repr__(self):
        return f"""User n°{self.id}
            email: {self.email},
            name: {self.name},
            birthday: {self.birthday},
            status: {self.status},
            creation_date: {self.creation_date},
            update_date: {self.update_date}"""
