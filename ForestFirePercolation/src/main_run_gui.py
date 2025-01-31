import tkinter as tk

from ForestFirePercolation.src.gui.initial_sim_select_gui import InitialSimSelectionGUI

def main():
    root = tk.Tk()
    
    InitialSimSelectionGUI(root)

    root.mainloop()

if __name__ == "__main__":
    main()