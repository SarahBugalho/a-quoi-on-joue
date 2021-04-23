from sqlalchemy import Column, DateTime, ForeignKey, Integer, String

from models import Base


class Game(Base):
    __tablename__ = "game"

    id = Column(Integer, primary_key=True)
    status = Column(String)
    name = Column(String)
    game_creation_year = Column(Integer)
    min_players = Column(Integer)
    max_players = Column(Integer)
    min_age = Column(Integer)
    collection_id = Column(Integer, ForeignKey("collection.id"), nullable=True)
    extension_of = Column(Integer, ForeignKey("game.id"), nullable=True)
    creation_date = Column(DateTime)
    update_date = Column(DateTime)

    def __repr__(self):
        return f"""Game n°{self.id}
            name: {self.name},
            game_creation_year: {self.game_creation_year},
            players: {self.min_players}-{self.max_players},
            min_age: {self.min_age},
            collection: collection n°{self.collection_id},
            extension_of: game n°{self.extension_of},
            creation_date: {self.creation_date},
            update_date: {self.update_date}"""
