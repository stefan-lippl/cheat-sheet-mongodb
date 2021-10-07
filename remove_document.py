# https://docs.mongodb.com/guides/server/delete/
from db_setup.db_connection import Connect


def main():
    """
    Remove documents
    """
    collection = Connect.get_connection().test.todos

    collection.delete_one({"name": "Bert"})  # delete more objects = delete_many()


if __name__ == main():
    main()
