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
    word_definition = {"success": False}
    # definition look up function will be added here
    word_definition["success"] = True
    word_definition["definition"] = "demo"
    print(word_definition)
    return word_definition
