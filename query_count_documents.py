# https://docs.mongodb.com/guides/server/read_queries/
from db_setup.db_connection import Connect


def main():
    """
    Query for multiple documents
    """
    collection = Connect.get_connection().test.todos

    results = collection.count_documents({})
    print(results)


if __name__ == main():
    main()
