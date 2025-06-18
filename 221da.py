import time
import tkinter as tk
from PIL import Image, ImageTk


time.sleep(3)


root = tk.Tk()
root.attributes('-fullscreen', True)  # На весь экран
root.configure(bg='black')
root.overrideredirect(True)  # Убирает заголовок и рамки окна


image_path = "OIP (6).jpg"
original_img = Image.open(image_path)
img = original_img.resize((100, 100))  # Размер каждой копии
tk_img = ImageTk.PhotoImage(img)


screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()


x_count = screen_width // 100
y_count = screen_height // 100

for x in range(x_count):
    for y in range(y_count):
        label = tk.Label(root, image=tk_img, borderwidth=0)
        label.place(x=x100, y=y100)

root.mainloop()
