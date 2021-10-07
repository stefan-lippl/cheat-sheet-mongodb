# https://docs.mongodb.com/guides/server/insert/
import datetime
import logging

from db_setup.db_connection import Connect


def main():
    """
    Insert a single document to the collection
    """
    connection = Connect.get_connection()
    print(connection.list_database_names())
    db = connection.test
    collection = db.todos

    try:
        collection.insert_one(
            {"name": "Albert",
             "text": "Code Review",
             "status": "open",
             "tags": ["c++", "coding"],
             "date": str(datetime.datetime.now())})
    finally:
        logging.info("Document successful created.")


if __name__ == main():
    main()
