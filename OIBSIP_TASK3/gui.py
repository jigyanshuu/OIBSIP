# gui.py

from PyQt5.QtWidgets import (
    QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QComboBox, QMessageBox, QFrame
)
from PyQt5.QtGui import QPixmap, QFont
from PyQt5.QtCore import Qt

from weather_api import fetch_current_weather
from utils import get_weather_icon
from config import DEFAULT_UNIT

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setFixedSize(400, 500)
        self.unit = DEFAULT_UNIT
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout()

        # Title
        title = QLabel("Weather Forecast")
        title.setFont(QFont("Arial", 20, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Input layout
        input_layout = QHBoxLayout()
        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter city name")
        input_layout.addWidget(self.city_input)

        self.unit_selector = QComboBox()
        self.unit_selector.addItems(["Celsius", "Fahrenheit"])
        input_layout.addWidget(self.unit_selector)

        self.search_button = QPushButton("Search")
        self.search_button.clicked.connect(self.search_weather)
        input_layout.addWidget(self.search_button)

        layout.addLayout(input_layout)

        # Separator
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        layout.addWidget(separator)

        # Weather icon
        self.icon_label = QLabel()
        self.icon_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.icon_label)

        # Weather info
        self.temp_label = QLabel("")
        self.temp_label.setFont(QFont("Arial", 16))
        self.temp_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.temp_label)

        self.details_label = QLabel("")
        self.details_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.details_label)

        self.setLayout(layout)

    def search_weather(self):
        city = self.city_input.text().strip()
        if not city:
            QMessageBox.warning(self, "Input Error", "Please enter a city name.")
            return

        unit_text = self.unit_selector.currentText()
        self.unit = "metric" if unit_text == "Celsius" else "imperial"

        data = fetch_current_weather(city, self.unit)

        if "error" in data:
            QMessageBox.critical(self, "Error", f"Could not fetch data:\n{data['error']}")
            return

        if data.get("cod") != 200:
            QMessageBox.warning(self, "City Not Found", data.get("message", "Unknown error"))
            return

        # Extract data
        temp = data['main']['temp']
        desc = data['weather'][0]['description'].capitalize()
        icon_path = get_weather_icon(data['weather'][0]['main'])

        self.icon_label.setPixmap(QPixmap(icon_path).scaled(100, 100, Qt.KeepAspectRatio))
        self.temp_label.setText(f"{temp}° {'C' if self.unit == 'metric' else 'F'}")
        self.details_label.setText(f"{desc}\nHumidity: {data['main']['humidity']}%\nWind: {data['wind']['speed']} m/s")
