import tkinter as tk
from pixel_gui import PixelGUI

def main():
    root = tk.Tk()
    app = PixelGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
