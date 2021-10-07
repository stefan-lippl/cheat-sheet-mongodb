from pymongo import MongoClient


class Connect(object):
    @staticmethod
    def get_connection():
        # Change <PW> with the personal mdb password
        return MongoClient("<DB_KEY>")
