from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QMessageBox, QGroupBox, QTextEdit
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from utils import calculate_bmi, categorize_bmi
from database import init_db, insert_record, fetch_history
from charts import BMIGraphWidget
import sys


def launch_gui():
    app = QApplication(sys.argv)
    window = BMICalculatorApp()
    window.show()
    sys.exit(app.exec_())


class BMICalculatorApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced BMI Calculator")
        self.setStyleSheet("background-color: #f9f9f9;")
        self.init_ui()
        init_db()

    def init_ui(self):
        # Fonts
        label_font = QFont("Arial", 10)
        result_font = QFont("Arial", 12, QFont.Bold)

        # Input fields
        self.height_input = QLineEdit()
        self.weight_input = QLineEdit()

        self.height_input.setPlaceholderText("Enter height in meters (e.g., 1.75)", )
        self.weight_input.setPlaceholderText("Enter weight in kilograms (e.g., 70)", )

        # Calculate button
        calc_button = QPushButton("Calculate BMI")
        calc_button.clicked.connect(self.calculate_bmi)

        # Result labels
        self.bmi_result = QLabel("")
        self.bmi_result.setFont(result_font)
        self.bmi_result.setAlignment(Qt.AlignCenter)

        self.interpretation_label = QLabel("")
        self.interpretation_label.setFont(result_font)
        self.interpretation_label.setAlignment(Qt.AlignCenter)

        # Health Advice label with link
        self.health_advice_label = QLabel("")
        self.health_advice_label.setWordWrap(True)
        self.health_advice_label.setOpenExternalLinks(True)
        self.health_advice_label.setStyleSheet("color: #555; font-size: 11px; padding: 10px; border: 1px solid #ccc; border-radius: 5px; background: #edf5ff;")
        self.health_advice_label.setAlignment(Qt.AlignLeft)

        # History box
        self.history_box = QTextEdit()
        self.history_box.setReadOnly(True)
        self.history_box.setPlaceholderText("BMI history will appear here...")

        # Trends widget
        self.trend_widget = BMIGraphWidget()

        # Layouts
        form_layout = QVBoxLayout()
        form_layout.addWidget(QLabel("Height (m):", font=label_font))
        form_layout.addWidget(self.height_input)
        form_layout.addWidget(QLabel("Weight (kg):", font=label_font))
        form_layout.addWidget(self.weight_input)
        form_layout.addWidget(calc_button)
        form_layout.addWidget(self.bmi_result)
        form_layout.addWidget(self.interpretation_label)
        form_layout.addWidget(self.health_advice_label)

        form_group = QGroupBox("BMI Calculator")
        form_group.setLayout(form_layout)

        history_group = QGroupBox("BMI History")
        history_layout = QVBoxLayout()
        history_layout.addWidget(self.history_box)
        history_group.setLayout(history_layout)

        trend_group = QGroupBox("BMI Trend")
        trend_layout = QVBoxLayout()
        trend_layout.addWidget(self.trend_widget)
        trend_group.setLayout(trend_layout)

        main_layout = QVBoxLayout()
        main_layout.addWidget(form_group)
        main_layout.addWidget(history_group)
        main_layout.addWidget(trend_group)

        self.setLayout(main_layout)
        self.setMinimumWidth(400)

    def calculate_bmi(self):
        try:
            height = float(self.height_input.text()) 
            weight = float(self.weight_input.text())    

            if height <= 0 or weight <= 0:
                raise ValueError

            bmi = calculate_bmi(weight, height)
            category = categorize_bmi(bmi)

            self.bmi_result.setText(f"Your BMI is: {bmi:.2f}")
            self.interpretation_label.setText(f"Category: {category}")

            # Provide health advice with link to WHO
            health_advices = {
                "Underweight": ("Consider a healthy diet rich in calories and nutrients.", "https://www.who.int/news-room/fact-sheets/detail/malnutrition"),
                "Normal weight": ("Keep up your healthy lifestyle!", "https://www.who.int/news-room/fact-sheets/detail/healthy-diet"),
                "Overweight": ("Consider lifestyle tweaks, a healthy diet, and adding physical activity.", "https://www.who.int/news-room/fact-sheets/detail/obesity"),
                "Obese": ("Seek guidance from a health professional.", "https://www.who.int/news-room/fact-sheets/detail/obesity")
            }

            advice, link = health_advices.get(category, ("General health guidance.", "https://www.who.int/"))
            self.health_advice_label.setText(f'{advice} <a href="{link}">Learn more</a>')

            insert_record(height, weight, bmi, category)
            # Refresh history
            self.history_box.clear()
            for record in fetch_history():
                timestamp, h, w, b, cat = record
                self.history_box.append(f"{timestamp} | H: {h}m | W: {w}kg | BMI: {b:.2f} | {cat}")

            self.trend_widget.plot_trend()

        except ValueError:
            QMessageBox.warning(self, "Invalid Input", "Please enter valid numerical values for height and weight.")


if __name__ == "__main__":
    launch_gui()
