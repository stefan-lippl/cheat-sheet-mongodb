# https://docs.mongodb.com/guides/server/read_queries/
from db_setup.db_connection import Connect
from bson.objectid import ObjectId


def main():
    """
    Query for a _id via ObjectID
    """
    collection = Connect.get_connection().test.todos

    result = collection.find_one({"_id": ObjectId('615ef44e142bc70dc065ef89')})
    print(result)


if __name__ == main():
    main()
