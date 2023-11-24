from kafka import KafkaConsumer, KafkaProducer
from fastapi import FastAPI
from datetime import date, timedelta, datetime
import uvicorn
import requests
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.statespace.sarimax import SARIMAX

#port 8000
api = "4714b0946cb4e14da77b6fc9cf316b40"
app = FastAPI()
current_date =date.today()
date_year = current_date - timedelta(days=365)

#producer = KafkaProducer()


@app.get("/forecast")
def forecast():
    print("Forecast")



def main():
    print("Today = ",current_date)
    print("Year = ", date_year)
    uvicorn.run(app, host="0.0.0.0", port=8000)


if __name__ == '__main__':
    main()
