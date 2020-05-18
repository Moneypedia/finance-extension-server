from fastapi import FastAPI
from datetime import date

# today's date
today_int = date.today()
print("test_app - Today's date:", today_int)

# Initializing Fast API
app = FastAPI()


@app.get("/")
def read_root():
    return {"connection": True}


@app.get("/proofread/{text}")
def word_receiver(text: str, q: str = None):
    word_definition = {"success": False}
    # definition look up function will be added here
    word_definition["success"] = True
    word_definition["definition"] = "demo"
    print(word_definition)
    return word_definition
