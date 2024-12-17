import tkinter as tk
from tkinter import messagebox
import random


def roll_dice():
    result = random.randint(1, 6)

    dice_image = dice_images[result - 1]
    label_image.config(image=dice_image)
    label_image.image = dice_image

window = tk.Tk()
window.title("Symulacja rzutu kostką")

dice_images = [tk.PhotoImage(file=f"dice{i}.png") for i in range(1, 7)]

label_result = tk.Label(window, text="Wynik: ", font=("Arial", 16))
label_result.pack(pady=10)

label_image = tk.Label(window)
label_image.pack(pady=10)

button_roll = tk.Button(window, text="Rzuć kostką", command=roll_dice, font=("Arial", 14))
button_roll.pack(pady=10)

window.mainloop()
