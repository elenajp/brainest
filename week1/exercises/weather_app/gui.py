from tkinter import *
from PIL import Image, ImageTk

root = Tk()

image = Image.open("background.jpg")
photo = ImageTk.PhotoImage(image)
width, height = image.size

canvas = Canvas(root, width=width, height=height)
canvas.create_image(0, 0, image=photo, anchor="nw", tags="bg")


def resize_image(event):
    global photo, resized_image
    new_width = event.width
    new_height = event.height
    resized_image = image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(resized_image)
    canvas.itemconfig("bg", image=photo)


canvas.bind("<Configure>", resize_image)

label = Label(canvas, text="Enter a city:", font=("Arial", 18))
canvas.create_window(
    root.winfo_screenwidth() / 2, root.winfo_screenheight() / 2, window=label
)
# label.pack(padx=20, pady=20)

button = Button(root, text="Enter", activebackground="teal")
button.pack(padx=10, pady=10)

# textbox = tk.Text(root, height=1, font=("Arial", 16), width=20)
# textbox.pack(padx=10, pady=10)

# city_input = tk.Entry(
#     root,
#     textvariable="city_value",
#     width=24,
#     font=("Arial", 16),
# )  # bg="#404040". fg="white"

canvas.pack()
root.mainloop()
