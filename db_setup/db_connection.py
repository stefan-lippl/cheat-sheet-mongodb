from pymongo import MongoClient


class Connect(object):
    @staticmethod
    def get_connection():
        return MongoClient("mongodb://stefan-lippl:<PASSWORD_HERE>$@cluster0-shard-00-00.301hm.mongodb.net:27017,"
                           "cluster0-shard-00-01.301hm.mongodb.net:27017,cluster0-shard-00-02.301hm.mongodb.net:27017/"
                           "test?ssl=true&replicaSet=atlas-luyu3t-shard-0&authSource=admin&retryWrites=true&w=majority")