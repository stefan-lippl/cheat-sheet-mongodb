# https://docs.mongodb.com/guides/server/update/
from db_setup.db_connection import Connect


def main():
    """
    Update documents
    """
    collection = Connect.get_connection().test.todos

    collection.update_one({"name": "Gerdtraud"}, {"$set": {"status": "open"}})


if __name__ == main():
    main()
