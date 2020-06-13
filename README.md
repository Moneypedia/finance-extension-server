## Installation
``` shell
pip install fastapi
```

You will also need an ASGI server, for production such as Uvicorn or Hypercorn.

``` shell
pip install uvicorn
```

Run it with command below.
All the other functions included in main.py will be run with the command line.

``` shell
uvicorn main:app --reload
```

### FastAPI Reference

* [FastAPI Usage](https://github.com/tiangolo/fastapi)
* [FastAPI Official Docs](https://fastapi.tiangolo.com/alternatives/)



## Deployment: Google Cloud Platform App Engine 

### Configuration & Installation

* [Tutorial Video Reference](https://www.youtube.com/watch?v=RaUO8mZJPN8)
* Creating Virtual Environment using Google Cloud Shell

```shell
git clone https://github.com/Moneypedia/finance-extension-server.git
cd financ-extension-server
virtualenv env
source env/bin/activate
pip install -r requirements.txt
export MONGO_URL="YOUR_MONGODB_ATLAS_URL"
uvicorn main:app --reload
```

### Creating Gcloud App

```shell
gcloud app create
gcloud app deploy app.yaml
gcloud app browse
gcloud app logs tail -s default
```

