from fastapi import FastAPI
from datetime import date
from connect_db import init_data


# today's date
today_int = date.today()
print("test_app - Today's date:", today_int)


# Initializing Fast API
app = FastAPI()

# Initializing Mongodb Atlas Connection
vocab_terms_collection = init_data()


@app.get("/")
def read_root():
    return {"connection": True}


@app.get("/lookup/{text}")
def word_receiver(text: str, q: str = None):
    one_json_doc = vocab_terms_collection.find_one({"vocabulary": text})
    # remove mongodb element id to prevent the following error
    # ValueError: [TypeError("'ObjectId' object is not iterable"), TypeError('vars() argument must have __dict__ attribute')]
    del one_json_doc["_id"]
    # print(one_json_doc)
    one_json_doc["server_response"] = True
    # print(one_json_doc)
    # print(type(one_json_doc))
    return one_json_doc
