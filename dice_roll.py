#             Task - 05  (" Dice Roll Simulator ")

import tkinter as tk
from PIL import Image, ImageTk
import random

window = tk.Tk()
window.geometry("400x360")
window.title("Dice Roll")


#program location dice location other location dice then use this code and dice name..
dice = ["C:/Users/hp/Pictures/dice/dice1.png","C:/Users/hp/Pictures/dice/dice2.png","C:/Users/hp/Pictures/dice/dice3.png",
        "C:/Users/hp/Pictures/dice/dice4.png","C:/Users/hp/Pictures/dice/dice5.png","C:/Users/hp/Pictures/dice/dice6.png",]

# the use dice location program to dice same program location then use this code.
# dice = ["dice1.png","dice2.png","dice3.png","dice4.png","dice5.png","dice6.png"]

image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1 = tk.Label(window,image=image1)
label2 = tk.Label(window,image=image2)

label1.image = image1
label2.image = image2

label1.place(x = 40, y = 100)
label2.place(x = 300, y = 100)

#create button 
def dice_roll():
    image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image = image1)
    label1.image = image1
    
    image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image = image2)
    label2.image = image2

button = tk.Button(window, text="ROLL",bg="green",fg="white",font="Times 20 bold",command=dice_roll)
button.place(x = 150, y = 0)

window.mainloop()



















# create the click button in the function inside..
# def roll_dice():
#    a = random.randint(1,6)
#    label = tk.Label(window,text=a).pack()
# button = tk.Button(window,text = "click", command=roll_dice)
# button.pack()



# import random

# again  = True

# while again:
#     print(random.randint(1, 6))
#     another_roll = input("Want to roll the dice again (y/n): ")
#     if another_roll.lower() == "y":
#         continue
#     else:
#         break

