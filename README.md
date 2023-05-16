# fastapi-playground
fastapi play ground

# Setup
## Virtual enviroment
- venv_fastapi
- pip install -r requirements.txt

## running
- uvicorn <filename>:<FastAPI instance name> 
```shell
uvicorn app:app --reload
```

# Dockerise
```shell
# build docker
docker build --tag fastapi-demo .

# run docker
docker run --detach --publish 3100:3100 fastapi-demo
```

# features
## self documenting
- http://127.0.0.1:8000/docs - Swagger
- http://127.0.0.1:8000/redoc - different format

# Tutorials
## Basic FastAPI
- [FastAPI Tutorial | FastAPI vs Flask](https://www.youtube.com/watch?v=Wr1JjhTt1Xg)
- [FastAPI official tutorial](https://fastapi.tiangolo.com/tutorial/)

## Dockerise FastAPI
- [Deploy a Flask or FastPI web app on Azure Container Apps](https://learn.microsoft.com/en-us/azure/developer/python/tutorial-containerize-simple-web-app?tabs=web-app-fastapi)

## Hosting in Azure container Apps
