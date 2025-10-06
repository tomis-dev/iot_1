# iot_1

This repository contains IoT course exercises and projects, organized by lesson and topic.

## Folder Overview

### Lesson_1

Contains various MicroPython and Wokwi simulator projects:

- **alarm/**: Simple alarm system example.
- **example_1** to **example_5/**: Basic sensor and actuator examples, each with a diagram and code.
- **reaction_game/**: Reaction game implementation.
- **trafficlights/**: Traffic light simulation.
- **weather_backend/**: Backend for weather data collection.
- **weather_station/**: Weather station project.

### Lesson_2

- **server.js**: Node.js server example for basic HTTP handling.

### Lesson_3

- **mydatabase.db**: Example SQLite database.
- **server2.js**: Node.js WebSocket server for real-time communication.

### Lesson_4

- **Fetch/**: Fetches temperature data and displays it in HTML.
- **GoogleChart/**: Visualizes fetched data using Google Charts.
- **Webhook/**: Example of using webhooks with Node.js.
- **Websocket/**: WebSocket client and server for real-time browser communication.

### Pipeline

A complete IoT data pipeline:

- **main.py**: MicroPython script for ESP32/ESP8266. Reads temperature and humidity, displays values on an LCD, sends data to ThingSpeak, and triggers Discord alerts if thresholds are exceeded.
- **config.py**: Configuration file for API keys and webhook URLs.
- **index.html**: Web dashboard using Chart.js. Fetches and visualizes ThingSpeak data, shows alerts if limits are exceeded.
- **diagram.json**: System diagram for the pipeline.

## How the Pipeline Works

1. **Data Collection**:  
   The ESP device runs `main.py`, reading temperature and humidity from a DHT22 sensor. Values are shown on an LCD.

2. **Data Upload**:  
   Sensor readings are sent to ThingSpeak (fields 1 and 2). If values exceed set thresholds, an alert flag (field 3) is set and a Discord webhook notification is triggered.

3. **Visualization**:  
   The web dashboard (`index.html`) fetches recent data from ThingSpeak and displays it using Chart.js. If the latest reading triggers an alert, a warning is shown on the page.

4. **Configuration**:  
   API keys and webhook URLs are managed in `config.py`.

---<img width="587" height="785" alt="Screenshot 2025-10-06 at 10 57 09" src="https://github.com/user-attachments/assets/02705874-2339-48a7-bcaa-c9acc352bd57" />
<img width="1175" height="736" alt="Screenshot 2025-10-06 at 11 05 39" src="https://github.com/user-attachments/assets/67ed4ede-7fb3-4c32-80fb-463680042697" />

