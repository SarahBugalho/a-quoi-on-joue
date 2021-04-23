from sqlalchemy import ARRAY, Column, DateTime, ForeignKey, Integer, String

from models import Base


class Collection(Base):
    __tablename__ = "collection"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    games_id = Column(ARRAY(Integer, ForeignKey("game.id")), nullable=True)
    creation_date = Column(DateTime)
    update_date = Column(DateTime)

    def __repr__(self):
        return f"""Collection n°{self.id}
            name: {self.name},
            games_id: {self.games_id},
            creation_date: {self.creation_date},
            update_date: {self.update_date}"""
