# https://docs.mongodb.com/guides/server/insert/
import datetime
from db_setup.db_connection import Connect


def main():
    """
    Insert a single document to the collection
    """
    connection = Connect.get_connection()
    print(connection.list_database_names())
    db = connection.test
    collection = db.todos

    collection.insert_one(
        {"name": "Maya",
         "text": "Bux fixes",
         "status": "open",
         "tags": ["python", "c++", "mongodb"],
         "date": str(datetime.datetime.now())})


if __name__ == main():
    main()
