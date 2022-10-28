import pymongo

from api.utils.constants import MONGO_URI, MONGODB_DATABASE, MONGODB_TESTS_COLLECTION


def create_database_connection(collection):
    if not database[MONGODB_DATABASE][collection]:
        database[MONGODB_DATABASE][collection] = pymongo.MongoClient(MONGO_URI)[MONGODB_DATABASE][MONGODB_TESTS_COLLECTION]
    return database[MONGODB_DATABASE][collection]



database = {
    MONGODB_DATABASE: {
        MONGODB_TESTS_COLLECTION: None
    }
}