# 🌦️ Advanced Weather Forecast App (OIBSIP Task 3)

This is a graphical weather forecast application built with **Python** and **PyQt5** as part of the **Oasis Infobyte Internship - Task 3**.

It allows users to:
- Search for current weather in any city
- View animated or static weather icons
- Switch between **light and dark themes**
- Toggle between **animated** and **static** weather icons
- Select between **Celsius** and **Fahrenheit** units

---

## 🛠️ Features

- 🔍 City-based weather search (via OpenWeatherMap API)
- 🌡️ Shows temperature, condition, wind speed
- 🌑 Dark Mode toggle
- 🎞️ Animated or static icon toggle (GIF/PNG)
- 📦 Modular structure with clean separation of concerns

---

## 📸 Preview

![App Screenshot](assets/preview/demo_screenshot.png)

> *Note: Include a screenshot of your app UI here*

---

## 🧩 Project Structure
    OIBSIP_TASK3/
    │
    ├── main.py # Main GUI application
    ├── config.py # API key storage
    ├── utils.py # Weather icon & data helpers
    │
    ├── assets/
    │ ├── icons/ # Static PNG weather icons
    │ └── animated_weather_icons/ # Animated GIF icons
    │
    └── README.md


---

## 🌍 How It Works

1. The user enters a city name.
2. The app fetches **real-time weather data** using the OpenWeatherMap API.
3. It then displays:
   - Temperature
   - Weather condition (e.g. Rain, Clear, Clouds)
   - Wind Speed
   - Corresponding weather icon (animated/static)

---

## ⚙️ Setup Instructions

1. **Clone the repository** or download the project folder:
   ```bash
   git clone https://github.com/your-username/OIBSIP_TASK3.git
   cd OIBSIP_TASK3


2. Install Dependencies
    pip install PyQt5 requests

3. Set your API key in config.py
     API_KEY = "your_openweathermap_api_key"

Run the app:
    python main.py


🔑 Get OpenWeatherMap API Key
    Visit: https://openweathermap.org/api
    Sign up for a free account.
    Navigate to API Keys and copy your key.
    Paste it into config.py.

🎨 Credits
Weather data powered by OpenWeatherMap
Animated icons sourced from public domain/weather icon libraries
Developed as part of Oasis Infobyte's Internship Program

🙌 Acknowledgments
Thanks to the mentors and contributors of the Oasis Infobyte internship for this wonderful opportunity!

🔹Developer
    Name: Jigyanshu Sabata
    Internship: OASIS Infobyte
    Github: jigyanshuu

📜License
This project is for educational purposes and a requirement for OASIS Infobyte internship.