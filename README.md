# 🌦️ Smart Weather Alert System (IoT + AI + SMS)

## 📌 Overview
This project is a Smart Weather Monitoring and Alert System that uses IoT sensors, a machine learning model, and a web application to detect weather changes and notify users via SMS.

The system collects real-time weather data, predicts changes, and automatically sends alerts to registered users.

---

## 🚀 Features
- 📡 Real-time weather monitoring using ESP32  
- 🤖 AI-based weather prediction  
- 🌐 Web dashboard built with React + Tailwind CSS  
- 🔐 User authentication (Signup/Login)  
- ☁️ Cloud database (MongoDB Atlas)  
- 📩 SMS alerts using Twilio  
- 📊 Weather data visualization  

---

## 🧠 How It Works

1. User Registration  
   - Users sign up with name, email, phone, and password  
   - Data is stored in the database  

2. Data Collection  
   - ESP32 collects:
     - Temperature  
     - Humidity  
     - Pressure  
     - Rain status  

3. Prediction  
   - ML model analyzes sensor data  
   - Detects weather changes (rain, storm, etc.)

4. Alert System  
   - When change is detected:
     - Backend fetches users  
     - SMS alerts are sent  

5. Dashboard  
   - Displays live data  
   - Shows predictions and alerts  

---

## 🛠️ Tech Stack

### Frontend
- React (Vite)
- Tailwind CSS  

### Backend
- Node.js  
- Express.js  

### Database
- MongoDB Atlas  

### IoT Hardware
- ESP32  
- DHT11 / DHT22 Sensor  
- Rain Sensor  

### Services
- Twilio (SMS Alerts)

---

---

## 📊 Future Improvements
- Location-based alerts  
- Advanced ML prediction  
- Mobile app integration  
- Push notifications  

---

## 👨‍💻 Author
Srihari Dev
sriharidev07@gmail.com

---

## ⭐ Contribution
Feel free to fork and contribute to this project.
