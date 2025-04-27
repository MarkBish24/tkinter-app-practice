from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title('Learn to code')

my_img1 = ImageTk.PhotoImage(Image.open('images/temp_image_01.png'))
my_img2 = ImageTk.PhotoImage(Image.open('images/temp_image_02.jpg'))
my_img3 = ImageTk.PhotoImage(Image.open('images/temp_image_03.jpg'))

image_list = [my_img1, my_img2, my_img3]

my_label = Label(image=my_img1)
my_label.grid(row=0, column=0, columnspan=3)

def back():
    global my_label
    global button_forward
    global button_back

def forward(image_number):
    global my_label
    global button_forward
    global button_back

    my_label.grid_forget()
    my_label = Label(image=image_list[image_number + 1]).grid(row=0, column=0, columnspan=3)
    button_forward = Button(root, text=">>", command)


button_back = Button(root, text="<<", command=lambda:back(2)).grid(row=1, column=0)
button_quit = Button(root, text='Exit Program', command=root.quit).grid(row=1, column=1)
button_forward =  Button(root, text='>>', command=lambda:forward(2)).grid(row=1, column=2)


root.mainloop()