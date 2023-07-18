#!/usr/bin/env python3
""" Mongo change school topics module.
"""


def update_topics(mongo_collection, name, topics):
    """ Python function that changes all topics of a school document based on the name.
        Arg:
            Prototype: def update_topics(mongo_collection, name, topics).
            mongo_collection will be the pymongo collection object
            name: Is the school name to update.
            topipcs: Is the list of topics approached in the school.
        Return:
            The update topics.
    """
    return mongo_collection.update_many({"name": name},
                                        {"$set": {"topics": topics}})
