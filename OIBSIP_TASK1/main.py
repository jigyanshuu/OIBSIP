def main():
    print("choose mode:")
    print("1. Simple (Tkinter)")
    print("2. Advanced (PyQt5)")
    
    choice=input("Enter 1 or 2: ")
    if choice=="1":
        import tkinter_mode
        tkinter_mode.launch_gui()
    elif choice=="2":
        import pyqt_mode
        pyqt_mode.launch_gui()
    else:
        print("Invalid Choice! Exiting...")

if __name__=="__main__":
    main()