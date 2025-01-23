import tkinter as tk
from gui.input_window import InputWindow

def main():
    root = tk.Tk()
    
    input_window = InputWindow(root)

    root.mainloop()

if __name__ == "__main__":
    main()