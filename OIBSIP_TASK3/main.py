import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel,
    QHBoxLayout, QLineEdit, QPushButton, QComboBox, QCheckBox
)
from PyQt5.QtGui import QFont, QMovie, QPixmap
from PyQt5.QtCore import Qt
from config import API_KEY
from utils import get_weather_icon


class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Weather App")
        self.setMinimumWidth(500)
        self.city = ""
        self.lat = None
        self.lon = None
        self.use_animated_icons = False

        self.init_ui()
        self.apply_theme(dark=False)  # default to light mode

    def init_ui(self):
        layout = QVBoxLayout()

        # Title
        title = QLabel("Weather Forecast")
        title.setFont(QFont("Arial", 18, QFont.Bold))
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Input Row
        input_layout = QHBoxLayout()
        self.city_input = QLineEdit()
        self.city_input.setPlaceholderText("Enter city name")

        self.unit_selector = QComboBox()
        self.unit_selector.addItems(["Celsius", "Fahrenheit"])

        search_btn = QPushButton("Search")
        search_btn.clicked.connect(self.fetch_weather)

        self.theme_toggle = QCheckBox("Dark Mode")
        self.theme_toggle.stateChanged.connect(self.toggle_theme)

        self.icon_toggle = QCheckBox("Animated Icons")
        self.icon_toggle.stateChanged.connect(self.toggle_icon_mode)

        input_layout.addWidget(self.city_input)
        input_layout.addWidget(self.unit_selector)
        input_layout.addWidget(search_btn)
        input_layout.addWidget(self.theme_toggle)
        input_layout.addWidget(self.icon_toggle)
        layout.addLayout(input_layout)

        # Result section
        self.result_layout = QVBoxLayout()
        self.weather_icon_label = QLabel()
        self.weather_icon_label.setAlignment(Qt.AlignCenter)

        self.weather_info_label = QLabel("Search a city to view weather.")
        self.weather_info_label.setAlignment(Qt.AlignCenter)
        self.weather_info_label.setFont(QFont("Arial", 12))

        self.result_layout.addWidget(self.weather_icon_label)
        self.result_layout.addWidget(self.weather_info_label)
        layout.addLayout(self.result_layout)

        self.setLayout(layout)

    def toggle_theme(self, state):
        self.apply_theme(dark=(state == Qt.Checked))

    def toggle_icon_mode(self, state):
        self.use_animated_icons = state == Qt.Checked

    def apply_theme(self, dark=False):
        if dark:
            self.setStyleSheet("""
                QWidget { background-color: #121212; color: white; }
                QLineEdit, QComboBox, QPushButton, QCheckBox {
                    background-color: #1f1f1f; color: white;
                }
            """)
        else:
            self.setStyleSheet("")

    def fetch_weather(self):
        self.city = self.city_input.text().strip()
        unit = self.unit_selector.currentText()
        units = "metric" if unit == "Celsius" else "imperial"

        if not self.city:
            self.weather_info_label.setText("Please enter a city name.")
            return

        try:
            url = f"http://api.openweathermap.org/data/2.5/weather?q={self.city}&appid={API_KEY}&units={units}"
            response = requests.get(url)
            data = response.json()

            if response.status_code != 200 or "main" not in data:
                self.weather_info_label.setText("Error fetching weather data.")
                print("DEBUG response:", data)
                return

            temp = data["main"]["temp"]
            desc = data["weather"][0]["description"].capitalize()
            wind = data["wind"]["speed"]
            icon_code = data["weather"][0]["main"]

            # Display data
            display_text = f"Weather in {self.city.title()}:\n\nTemperature: {temp}°{unit[0]}\nCondition: {desc}\nWind Speed: {wind} m/s"
            self.weather_info_label.setText(display_text)

            # Set icon (animated or static)
            icon_path = get_weather_icon(icon_code, animated=self.use_animated_icons)

            if self.use_animated_icons and icon_path.endswith(".gif"):
                movie = QMovie(icon_path)
                self.weather_icon_label.setMovie(movie)
                movie.start()
            else:
                pixmap = QPixmap(icon_path).scaled(100, 100, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                self.weather_icon_label.setPixmap(pixmap)

        except Exception as e:
            self.weather_info_label.setText("Error retrieving data.")
            print("Error:", e)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = WeatherApp()
    window.show()
    sys.exit(app.exec_())
