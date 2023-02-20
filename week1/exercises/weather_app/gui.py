# Use the tkinter library to create a GUI for the app, including widgets such as labels, buttons and text boxes.

# Enter city: rome
# [{'description': 'overcast clouds', 'icon': '04d', 'id': 804, 'main': 'Clouds'}]

import tkinter as tk

# from weather_app import get_current_weather

root = tk.Tk()
root.geometry("500x500")  # how to make it change with the screen size
root.title("Weather App")

label = tk.Label(root, text="Hello World!", font=("Arial", 18))
label.pack(padx=20, pady=20)

textbox = tk.Text(root, height=3, font=("Arial", 16))
textbox.pack(padx=10, pady=10)

button = tk.Button(root, text="Enter")
button.pack(padx=10, pady=10)

root.mainloop()
