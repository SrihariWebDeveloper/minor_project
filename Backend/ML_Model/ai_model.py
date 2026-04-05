import requests
import pandas as pd
import numpy as np
import joblib
import threading
import time
from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token,jwt_required
from db import users_collection
from alert_sender import notify_users


app = Flask(__name__)
CORS(app)

app.config["JWT_SECRET_KEY"] = "srihari"

jwt = JWTManager(app)


READ_API_KEY = 'KEPLLQ6PUE23FB5F'
CHANNEL_ID = '3239627'
model = joblib.load("model/weather_model.pkl")


def predict_rain(temperature_celsius, humidity, pressure_mb, wind_kph):
    X = pd.DataFrame([{
        "temperature_celsius": temperature_celsius,
        "humidity": humidity,
        "pressure_mb": pressure_mb,
        "wind_kph": wind_kph
    }])
    prediction = model.predict(X)[0]
    probability = model.predict_proba(X)[0][1]
    return prediction, probability


def generate_alert(temperature_celsius, humidity, pressure_mb, wind_kph):
    rain_pred, rain_prob = predict_rain(temperature_celsius, humidity, pressure_mb, wind_kph)

    alerts = []

    if rain_prob > 0.7:
        alerts.append("Heavy rainfall alert")

    if wind_kph > 40:
        alerts.append("Strong wind alert")

    if temperature_celsius > 40:
        alerts.append("Heatwave warning")

    if not alerts:
        alerts.append("Weather is normal")

    return alerts


# --- Fetch data ---
url = f"https://api.thingspeak.com/channels/{CHANNEL_ID}/feeds.json?api_key={READ_API_KEY}&results=1"
response = requests.get(url).json()

feed = response["feeds"][0]

# Convert safely
temperature_celsius = float(feed["field1"])
humidity = float(feed["field2"])
wind_kph = float(feed["field3"])
pressure_mb = float(feed["field4"])

# --- Predict ---
rain_pred, rain_prob = predict_rain(temperature_celsius, humidity, pressure_mb, wind_kph)
alerts = generate_alert(temperature_celsius, humidity, pressure_mb, wind_kph)


def get_weather_data():
     return {
        "temperature": temperature_celsius,
        "humidity": humidity,
        "pressure": pressure_mb,
        "wind_speed": wind_kph
    }


def generate_alert():
    return alerts
# print("Rain prediction:", rain_pred)
# print("Rain probability:", rain_prob)
# print("Alerts:", alerts)

@app.route("/")
def heath():
    return jsonify({
        "message": "API is working"
    })

@app.route("/signup", methods=["POST"])
def signup():

    data = request.json

    username = data["username"]
    email = data["email"]
    mobile = data["mobile"]
    password = data["password"]

    hashed_password = generate_password_hash(password)

    user = {
        "username": username,
        "email": email,
        "mobile": mobile,
        "password": hashed_password
    }

    users_collection.insert_one(user)

    return jsonify({
        "success": True,
        "message": "User registered successfully"
    })


# -----------------------
# Login API
# -----------------------
@app.route("/login", methods=["POST"])
def login():

    data = request.json

    email = data["email"]
    password = data["password"]

    user = users_collection.find_one({"email": email})

    if user and check_password_hash(user["password"], password):

        token = create_access_token(identity=email)

        return jsonify({
            "success": True,
            "token": token
        })

    return jsonify({"success": False})

def background_weather_alert():
    while True:
        weather = get_weather_data()
        alert = generate_alert()

        print("Weather:", weather)
        print("Alert:", alert)

        # Send SMS only if severe alert
        if "Heavy rain" in alert or "Heatwave" in alert or "Strong wind" in alert:
            notify_users(alert)
            print("Message sent")

        time.sleep(5)  # run every 5 seconds

# -----------------------
# Start Background Thread
# -----------------------
threading.Thread(target=background_weather_alert, daemon=True).start()

# -----------------------
# Weather API
# -----------------------
@app.route("/weather", methods=["GET"])
def weather():

    weather_data = get_weather_data()

    alert = generate_alert()

    response = {
        "temperature": weather_data["temperature"],
        "humidity": weather_data["humidity"],
        "pressure": weather_data["pressure"],
        "wind_speed": weather_data["wind_speed"],
        "alert": alert
    }

    return jsonify(response)

# -----------------------
# Run server
# -----------------------
if __name__ == "__main__":
    app.run(debug=True, port=5000)