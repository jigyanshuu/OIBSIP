# OIBSIP_TASK1 - BMI Calculator Project

## 📚 Project Description

This **BMI Calculator** is a **GUI application** implemented in **Python with PyQt5**.  
It allows users to:

- Input their **height (m)** and **weight (kg)**.
- Calculate their **BMI (Body Mass Index)**.
- View their BMI alongside health categorizations.
- Store their BMI history in a local SQLite database.
- Visualize their BMI trends over time with a graph.
- Provide health advice and helpful links related to their BMI category.

This project is a part of my **Internship with OASIS Infobyte**.  
It’s the first of **3 projects** I’m developing during this internship.

---

## 🛠 Tech Stack

- **Python 3.x**
- **PyQt5** for GUI
- **Matplotlib** for data visualization
- **sqlite3** for database storage

---

## 🔹Features

✅ Calculate BMI with health categorizations  
✅ Store BMI history in a SQLite database  
✅ View BMI trends over time with a graph  
✅ Provide health advice for each BMI category  
✅ Link to external health resources (WHO)

---

## ⚡ Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/OIBSIP_TASK1.git
cd OIBSIP_TASK1

2. Create a virtual environment 
python -m venv .venv
source .venv/Scripts/activate  # for cmd or PowerShell

3. Install Dependencies:
pip install PyQt5 matplotlib

🚀 How to Run
python main.py
Select 1 for Tkinter (Simple) or 2 for PyQt5 (Advanced).

Enter your height in m and weight in kg.

The application will compute BMI, show its health category, and store it in the database.

🏹 File Structure

OIBSIP_TASK1/
 ├── main.py
 ├── tkinter_mode.py
 ├── pyqt_mode.py
 ├── charts.py
 ├── database.py
 ├── utils.py
 └── README.md

 🔹Developer
Name: Jigyanshu Sabata

Internship: OASIS Infobyte

Github: jigyanshuu

📜License
This project is for educational purposes and a requirement for OASIS Infobyte internship.