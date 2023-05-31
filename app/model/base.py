from flask import current_app


class MongoModel:
    collection_name = None

    @classmethod
    def get_collection(cls):
        if not cls.collection_name:
            raise NotImplementedError('No collection name set for this model.')
        return current_app.mongo.client[cls.collection_name]

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

    @classmethod
    def insert_many(cls, documents):
        cls.get_collection().insert_many(documents)

    @classmethod
    def delete(cls, query):
        cls.get_collection().delete_one(query)

    @classmethod
    def delete_many(cls, query):
        cls.get_collection().delete_many(query)

    @classmethod
    def update(cls, query, update):
        cls.get_collection().update_one(query, update)

    @classmethod
    def update_many(cls, query, update):
        cls.get_collection().update_many(query, update)

    @classmethod
    def aggregate(cls, pipeline):
        return cls.get_collection().aggregate(pipeline)

    @classmethod
    def count(cls, query):
        return cls.get_collection().count(query)

    def __init__(self, document=None):
        if document is None:
            document = {}
        self.document = document
