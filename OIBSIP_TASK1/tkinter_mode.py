import tkinter as tk
from tkinter import messagebox
from utils import calculate_bmi, categorize_bmi
def launch_gui():
    def on_calculate():
        try:
            h=float(height_entry.get())
            w=float(weight_entry.get())
            bmi=calculate_bmi(w,h)
            result_label.config(text=f"Cateogry: {categorize_bmi(bmi)}")
            interpretation_label.config(text=f"Category: {categorize_bmi(bmi)}")
        except ValueError:
            messagebox.showerror("Error","Enter valid numbers")
    window=tk.Tk()
    window.title("Simple Bmi calculator")
   
    tk.Label(window, text="Height (m):").pack
    height_entry=tk.Entry(window)
    height_entry.pack()
    
    tk.Label(window, text="Weight (kg):").pack()
    weight_entry=tk.Entry(window)
    weight_entry.pack()
    
    tk.Button(window, text="Calculate", command=on_calculate).pack()
    result_label=tk.Label(window, text="")
    result_label.pack()
    interpretation_label=tk.Label(window, text="")
    interpretation_label.pack()
    
    window.mainloop()
    
    
    