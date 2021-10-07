# https://docs.mongodb.com/guides/server/insert/
from db_setup.db_connection import Connect


def main():
    """
    Query for one item in the collection todos
    """
    collection = Connect.get_connection().test.todos

    result = collection.find_one({})
    print(result)


if __name__ == main():
    main()
