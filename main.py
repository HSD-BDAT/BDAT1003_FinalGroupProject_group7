#%% Import Packages
import requests
# import time
from pymongo import MongoClient
import pandas as pd
from flask import Flask, render_template
   
app = Flask(__name__)


#----------------------------------------------------------------------------#
#%% Connect with Mongo Db
#Step 1: Connect to MongoDB - Note: Change connection string as needed
client = MongoClient("mongodb+srv://bdatAdmin:HCjquZSkonIiojmi@cluster0.zbfiq.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
db = client.airPollution

#----------------------------------------------------------------------------#
#%% Load Data
#while True:
r1 = requests.get("https://api.waqi.info/feed/barrie/?token=145eb682b3161323b0a7f475248603022e99fe97")
r2 = requests.get("https://api.waqi.info/feed/toronto/?token=145eb682b3161323b0a7f475248603022e99fe97")
r3 = requests.get("https://api.waqi.info/feed/calgary/?token=145eb682b3161323b0a7f475248603022e99fe97")
r4 = requests.get("https://api.waqi.info/feed/vancouver/?token=145eb682b3161323b0a7f475248603022e99fe97")
r5 = requests.get("https://api.waqi.info/feed/delhi/?token=145eb682b3161323b0a7f475248603022e99fe97")

#%% Summary
@app.route('/')
def home():
    barrie = r1.json()
    toronto = r2.json()
    calgary = r3.json()
    vancouver = r4.json()
    delhi = r5.json()
    result = db.Barrie.insert_one(barrie)
    return render_template('pages/homePage.html', **locals())

#%% Barrie
@app.route('/barrie')
def barrie():
    barrie = r1.json()
    aqi = barrie['data']['aqi'] 
    c = 'AQI'
    dateTime = barrie['data']['time']['iso']
    MainPollutant = barrie['data']['dominentpol']
    coords = barrie['data']['city']['geo']
    cityName = barrie['data']['city']['name']
    iaqi = barrie['data']['iaqi'] 
    iaqi = pd.json_normalize(iaqi)
    
    ozoneForecast = pd.json_normalize(barrie['data']['forecast']['daily']['o3'])
    pm10_forecast = pd.json_normalize(barrie['data']['forecast']['daily']['pm10'])
    pm2_5_forecast = pd.json_normalize(barrie['data']['forecast']['daily']['pm25'])
    uv_Index_forecast = pd.json_normalize(barrie['data']['forecast']['daily']['uvi'])

    return render_template('pages/Barrie.html', **locals())   
 
#%% Toronto
@app.route('/toronto')
def toronto():
    toronto = r2.json()
    aqi = toronto['data']['aqi'] 
    c = 'AQI'
    dateTime = toronto['data']['time']['iso']
    MainPollutant = toronto['data']['dominentpol']
    coords = toronto['data']['city']['geo']
    cityName = toronto['data']['city']['name']
    iaqi = toronto['data']['iaqi'] 
    iaqi = pd.json_normalize(iaqi)
    
    ozoneForecast = pd.json_normalize(toronto['data']['forecast']['daily']['o3'])
    pm10_forecast = pd.json_normalize(toronto['data']['forecast']['daily']['pm10'])
    pm2_5_forecast = pd.json_normalize(toronto['data']['forecast']['daily']['pm25'])
    uv_Index_forecast = pd.json_normalize(toronto['data']['forecast']['daily']['uvi'])

    return render_template('pages/Toronto.html', **locals())

#%% Calgary
@app.route('/calgary')
def calgary():
    calgary = r3.json()
    aqi = calgary['data']['aqi'] 
    c = 'AQI'
    dateTime = calgary['data']['time']['iso']
    MainPollutant = calgary['data']['dominentpol']
    coords = calgary['data']['city']['geo']
    cityName = calgary['data']['city']['name']
    iaqi = calgary['data']['iaqi'] 
    iaqi = pd.json_normalize(iaqi)
    
    ozoneForecast = pd.json_normalize(calgary['data']['forecast']['daily']['o3'])
    pm10_forecast = pd.json_normalize(calgary['data']['forecast']['daily']['pm10'])
    pm2_5_forecast = pd.json_normalize(calgary['data']['forecast']['daily']['pm25'])
    uv_Index_forecast = pd.json_normalize(calgary['data']['forecast']['daily']['uvi'])

    return render_template('pages/Calgary.html', **locals())

#%% Vancouver
@app.route('/vancouver')
def vancouver():
    vancouver = r4.json()
    aqi = vancouver['data']['aqi'] 
    c = 'AQI'
    dateTime = vancouver['data']['time']['iso']
    MainPollutant = vancouver['data']['dominentpol']
    coords = vancouver['data']['city']['geo']
    cityName = vancouver['data']['city']['name']
    iaqi = vancouver['data']['iaqi'] 
    iaqi = pd.json_normalize(iaqi)
    
    ozoneForecast = pd.json_normalize(vancouver['data']['forecast']['daily']['o3'])
    pm10_forecast = pd.json_normalize(vancouver['data']['forecast']['daily']['pm10'])
    pm2_5_forecast = pd.json_normalize(vancouver['data']['forecast']['daily']['pm25'])
    uv_Index_forecast = pd.json_normalize(vancouver['data']['forecast']['daily']['uvi'])

    return render_template('pages/Vancouver.html', **locals())

#%% Delhi
@app.route('/newdelhi')
def newdelhi():
    delhi = r5.json()
    aqi = delhi['data']['aqi'] 
    c = 'AQI'
    dateTime = delhi['data']['time']['iso']
    MainPollutant = delhi['data']['dominentpol']
    coords = delhi['data']['city']['geo']
    cityName = delhi['data']['city']['name']
    iaqi = delhi['data']['iaqi'] 
    iaqi = pd.json_normalize(iaqi)
    
    ozoneForecast = pd.json_normalize(delhi['data']['forecast']['daily']['o3'])
    pm10_forecast = pd.json_normalize(delhi['data']['forecast']['daily']['pm10'])
    pm2_5_forecast = pd.json_normalize(delhi['data']['forecast']['daily']['pm25'])
    uv_Index_forecast = pd.json_normalize(delhi['data']['forecast']['daily']['uvi'])

    return render_template('pages/NewDelhi.html', **locals())

#%% Barrie Forecast
@app.route('/forecast')
def forecast():
    barrie = r1.json()
    aqi = barrie['data']['aqi'] 
    c = 'AQI'
    dateTime = barrie['data']['time']['iso']
    MainPollutant = barrie['data']['dominentpol']
    coords = barrie['data']['city']['geo']
    cityName = barrie['data']['city']['name']
    iaqi = barrie['data']['iaqi'] 
    iaqi = pd.json_normalize(iaqi)
    
    ozoneForecast = pd.json_normalize(barrie['data']['forecast']['daily']['o3'])
    pm10_forecast = pd.json_normalize(barrie['data']['forecast']['daily']['pm10'])
    pm2_5_forecast = pd.json_normalize(barrie['data']['forecast']['daily']['pm25'])
    pm2_5_forecast = pm2_5_forecast[['day', 'avg', 'max', 'min']]
    pm = pm2_5_forecast.to_numpy().tolist()
    uv_Index_forecast = pd.json_normalize(barrie['data']['forecast']['daily']['uvi'])
    
    return render_template('pages/forecast.html', **locals())    
  
#%% About
@app.route('/about')
def about():
    return render_template('pages/about.html')

#%%
if __name__ == "__main__":
    app.run(debug = True)   
    
    
    
# time.sleep(500)    