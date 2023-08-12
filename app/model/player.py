from app.model.base import MongoModel


class Player(MongoModel):
    collection_name = "players"

    @classmethod
    def get_player(cls, player_id):
        return cls.find({"_id": player_id})

    @classmethod
    def get_players_pagination(cls, page, limit):
        return cls.find_pagination({}, page, limit)
