# ui/current_weather.py
from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt
import requests
from config import API_KEY
from utils import format_icon

class CurrentWeatherWidget(QWidget):
    def __init__(self, city, unit='metric'):
        super().__init__()
        self.city = city
        self.unit = unit
        self.initUI()

    def initUI(self):
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)

        # Fetch weather data
        url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&units={self.unit}&appid={API_KEY}"
        response = requests.get(url)

        if response.status_code != 200:
            layout.addWidget(QLabel("Error fetching weather data."))
            self.setLayout(layout)
            return

        data = response.json()
        temp = data['main']['temp']
        description = data['weather'][0]['description']
        icon = data['weather'][0]['main'].lower()
        city_name = data['name']
        country = data['sys']['country']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']

        # Weather icon
        icon_path = format_icon(icon, animated=True)
        icon_label = QLabel()
        pixmap = QPixmap(icon_path).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
        icon_label.setPixmap(pixmap)

        # Labels
        location_label = QLabel(f"{city_name}, {country}")
        location_label.setFont(QFont("Arial", 18, QFont.Bold))

        temp_label = QLabel(f"{temp}°")
        temp_label.setFont(QFont("Arial", 40))

        desc_label = QLabel(description.title())
        desc_label.setFont(QFont("Arial", 14))

        details_label = QLabel(f"Humidity: {humidity}%\nWind Speed: {wind_speed} m/s")
        details_label.setFont(QFont("Arial", 12))

        layout.addWidget(location_label, alignment=Qt.AlignCenter)
        layout.addWidget(icon_label, alignment=Qt.AlignCenter)
        layout.addWidget(temp_label, alignment=Qt.AlignCenter)
        layout.addWidget(desc_label, alignment=Qt.AlignCenter)
        layout.addWidget(details_label, alignment=Qt.AlignCenter)

        self.setLayout(layout)
