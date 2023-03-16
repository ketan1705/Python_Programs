from tkinter import *
#for jpg image
from PIL import Image,ImageTk

ketan_root = Tk()

#width  X height
ketan_root.geometry("733x434")

# width, height
ketan_root.minsize(733,434)
ketan_root.maxsize(733,434)

anik = Label(text="First practice")
anik.pack()

#for png image
photo1 = PhotoImage(file="1.png")
manku_label= Label(image=photo1)
manku_label.pack()

# for jpg image and other image
#image = Image.open("audi3.jpg")
#photo = ImageTk.PhotoImage(image)

#ani_label = Label(image = photo)
#ani_label.pack()

#for change the title

ketan_root.title("First GUI")

ketan_root.mainloop()
