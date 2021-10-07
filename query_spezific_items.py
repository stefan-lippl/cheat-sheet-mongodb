# https://docs.mongodb.com/guides/server/read_queries/
from db_setup.db_connection import Connect


def main():
    """
    Query for a specific item
    """
    collection = Connect.get_connection().test.todos

    result = collection.find_one({"name": "Gerdtraud"})
    print(result)


if __name__ == main():
    main()
