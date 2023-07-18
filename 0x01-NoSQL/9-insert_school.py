#!/usr/bin/env python3
""" Python function that inserts a new document in a collection
"""


def insert_school(mongo_collection, **kwargs):
    """ Method that inserts a new document in a collection based on kwargs.
        Arg:
            rototype: def insert_school(mongo_collection, **kwargs)
        Return:
            The new _id.
    """
    insert_document = mongo_collection.insert_one(kwargs)
    return insert_document.inserted_id
