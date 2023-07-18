#!/usr/bin/env python3
""" a Python function that lists all documents in a collection:
"""


def list_all(mongo_collection):
    """ Method that lists all documents in a collection.
        Arg:
            Prototype: def list_all(mongo_collection).
        Return:
            An empty list if no document in the collection.
    """
    return mongo_collection.find()
