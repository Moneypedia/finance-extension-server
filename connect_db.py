import pymongo
import os


def init_data() -> None:
    # using dotenv to fetch MongoDB Atlas URL environment variable
    MONGO_URL = os.getenv("MONGO_URL")
    # print("Connecting MongoDB Atlas to: " + MONGO_URL)

    # accessing MongoDB Atlas with pymongo MongoClient
    client = pymongo.MongoClient(MONGO_URL)

    # connect to the mongodb atlas database and collection
    vocab_db = client.get_database("vocab")
    vocab_terms_collection = vocab_db.vocab_terms

    # testing collection connection
    db = client.get_database("vocab")
    vocab_terms_mongodb = db.vocab_terms
    all_documents_number = str(vocab_terms_mongodb.count_documents({}))

    print("Currently total " + all_documents_number + " exists in database")

    return vocab_terms_collection
