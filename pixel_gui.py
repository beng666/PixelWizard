import tkinter as tk
from PIL import Image, ImageTk
from PixelProcessor import PixelProcessor

class PixelGUI:
    def __init__(self, master):
        self.master = master
        master.title('Pixel')
        self.screen_width = master.winfo_screenwidth()
        self.screen_height = master.winfo_screenheight()
        master.geometry(f"{self.screen_width}x{self.screen_height}+0+0")

        self.canvas = tk.Canvas(master, width=self.screen_width, height=self.screen_height)
        self.canvas.pack()

        self.set_background()

        self.create_buttons()

    def set_background(self):
        background_image = Image.open("bum.jpg")  # Change the background image filename here
        background_photo = ImageTk.PhotoImage(background_image)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=background_photo)
        self.canvas.image = background_photo  # Keep a reference to avoid garbage collection

    def upload_image(self):
        # You can include PixelProcessor without displaying the Pikachu image here
        image_path = "pikachuu.png"  # Change the image filename here
        image_processor = PixelProcessor()
        image_processor.extract_pixels(image_path)

        # You can continue updating the UI based on the results of image processing

    def create_buttons(self):
        upload_button = tk.Button(self.canvas, text="UPLOAD", bg="#5C6BC0", fg="black", font=("Arial", 20), command=self.upload_image)
        upload_button.place(x=750, y=370, anchor="center")

# Commenting out the instantiation and method calls
# root = tk.Tk()
# app = PixelGUI(root)
# root.mainloop()
