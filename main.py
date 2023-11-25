import json

from kafka import KafkaConsumer, KafkaProducer
from fastapi import FastAPI
from datetime import date, timedelta, datetime
import uvicorn
import requests
from pymongo import MongoClient

from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()
origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

current_date = date.today()
date_year = current_date - timedelta(days=365)

client = MongoClient('mongodb://localhost:27017/')
db = client['QuotesDB']


def recharge_data(documents):
    data_up = [doc for doc in documents]
    data = []
    for i in range(len(data_up)):
        del data_up[i]['_id']
        data_up[i]['date'] = str(data_up[i]['date'])
        data.append(data_up[i])
    print(data)
    json_data = json.dumps(data)
    print(json_data)
    return data


@app.get("/forecast/gold")
def forecast_gold():
    print("Forecast gold")
    collection = db['forecastGold']
    documents = collection.find()
    return recharge_data(documents)
    #return {"mess": "gg"}


@app.get("/forecast/brent")
def forecast_brent():
    print("Forecast oil ")
    collection = db['forecastBrent']
    documents = collection.find()
    return recharge_data(documents)


@app.get("/forecast/cuprum")
def forecast_cuprum():
    print("Forecast cuprum ")
    collection = db['forecastCuprum']
    documents = collection.find()
    return recharge_data(documents)

@app.get("/forecast/dollar")
def forecast_dollar():
    print("Forecast dollar ")
    collection = db['forecastDollar']
    documents = collection.find()
    return recharge_data(documents)

@app.get("/forecast/imoex")
def forecast_imoex():
    print("Forecast imoex ")
    collection = db['forecastImoex']
    documents = collection.find()
    return recharge_data(documents)

def main():
    print("Today = ", current_date)
    print("Year = ", date_year)
    uvicorn.run(app, host="localhost", port=8000)


if __name__ == '__main__':
    main()
