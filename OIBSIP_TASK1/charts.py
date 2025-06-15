import matplotlib
matplotlib.use("QT5Agg")  # This lets us render within PyQT5
from PyQt5.QtWidgets import QWidget, QVBoxLayout
from matplotlib.figure import Figure
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas

from database import fetch_history


class BMIGraphWidget(QWidget):
    """Displays BMI trends over time in a graph format."""
    def __init__(self, parent=None):
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

    def plot_trend(self):
        """Plot BMI trends over time."""
        history = fetch_history()
        dates = [item[0] for item in history]
        bmis = [item[3] for item in history]

        self.figure.clear()
        ax = self.figure.add_subplot(111)
        ax.plot(dates, bmis, marker='o', color='skyblue')
        ax.set_title("BMI Trends")
        ax.set_xlabel("Dates")
        ax.set_ylabel("BMI")

        ax.grid(True)
        self.canvas.draw()
