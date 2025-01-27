import tkinter as tk
from gui.sim_selection import SimSelection

def main():
    root = tk.Tk()
    
    SimSelection(root)

    root.mainloop()

if __name__ == "__main__":
    main()