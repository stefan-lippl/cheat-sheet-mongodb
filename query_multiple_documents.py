# https://docs.mongodb.com/guides/server/read_queries/
from db_setup.db_connection import Connect


def main():
    """
    Query for multiple documents
    """
    collection = Connect.get_connection().test.todos

    # results = collection.find({"tags": "python"})
    results = collection.find({})
    for result in results:
        print(result)


if __name__ == main():
    main()
