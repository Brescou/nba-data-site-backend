from flask import current_app

class MongoModel:
    collection_name = None

    @classmethod
    def get_collection(cls):
        if not cls.collection_name:
            raise NotImplementedError('No collection name set for this model.')
        return current_app.mongo.db[cls.collection_name]

    @classmethod
    def find(cls, query):
        result = cls.get_collection().find_one(query)
        if result:
            return cls(result)
        return None

    @classmethod
    def find_all(cls):
        return [cls(item) for item in cls.get_collection().find()]

    @classmethod
    def insert(cls, document):
        cls.get_collection().insert_one(document)

    def __init__(self, document):
        self.document = document
