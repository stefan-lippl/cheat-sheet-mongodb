# https://docs.mongodb.com/guides/server/read_queries/
from db_setup.db_connection import Connect
import datetime


def main():
    """
    Query in a specific range
    """
    collection = Connect.get_connection().test.todos

    d = datetime.datetime(2021, 2, 1)
    results = collection.find({"date": {"$gt": d}})  # lt = less then,gt = greater then
    for result in results:
        print(result)


if __name__ == main():
    main()
