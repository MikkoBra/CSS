import tkinter as tk

from ForestFirePercolation.src.gui.initial_sim_select_gui import InitialSimSelectionGUI

"""
Main function to run the GUI for the Forest Fire Percolation model.
"""
def main():
    root = tk.Tk()
    
    InitialSimSelectionGUI(root)

    root.mainloop()

if __name__ == "__main__":
    main()