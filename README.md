# fastapi-playground
fastapi play ground

# Setup
## Virtual enviroment
- venv_fastapi
- pip install -r requirements.txt

## Local Running
- uvicorn <filename>:<FastAPI instance name> 
```shell
uvicorn app:app --reload
```

# Dockerise
```shell
# build docker
docker build --tag fastapi-randdemo .

# run docker
docker run --detach --publish 3100:3100 fastapi-randdemo
```

# Host in Azure ContainerApps
## login to Azure cloud
```shell
az login --use-device-code

# note down the code in cli
# open browser with url https://microsoft.com/devicelogin and add the code with your admin login to azure portal
```

## container app creation and hosting
```shell
# Deploy container app
az containerapp up --resource-group RG-web-fastapi-aca --name web-aca-app --ingress external --target-port 3100 --source .

## Stream logs for your container with: 
az containerapp logs show -n web-aca-app -g RG-web-fastapi-aca

## See full output using: 
az containerapp show -n web-aca-app -g RG-web-fastapi-aca
```

## cleanup
```shell
az group delete --name RG-web-fastapi-aca
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
- 
