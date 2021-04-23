from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String

from models import Base


class Friendship(Base):
    __tablename__ = "friendship"

    user_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    friend_id = Column(Integer, ForeignKey("user.id"), primary_key=True)
    status = Column(String)
    lend_game = Column(Boolean)
    creation_date = Column(DateTime)
    update_date = Column(DateTime)

    def __repr__(self):
        return f"""Friendship user n°{self.user_id} -> user n°{self.friend_id}
            status:{self.status},
            lend_game:{self.lend_game},
            creation_date:{self.creation_date},
            update_date:{self.update_date}"""
