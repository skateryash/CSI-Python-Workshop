# Part 1: Creating window and label

# import tkinter
from tkinter import *

window = Tk()
window.title("First Desktop Application")
window.minsize(width=500, height=300)

# Label                  Doc: https://tcl.tk/man/tcl8.6/TkCmd/pack.htm

my_label = Label(text="I am a Label", font=("Arial", 24, "bold"), bg="Yellow")
# my_label.pack()

# my_label["text"] = "New Text"
# my_label.config(text="New Text 123")


# Entry                  Doc: https://tcl.tk/man/tcl8.6/TkCmd/entry.htm

input = Entry(width=30)
# input.pack()
# user_input = input.get()



# Button

def button_clicked():
    print("I got clicked")
    # my_label.config(text="Button Got Clicked by Yash")
    user_input = input.get()
    my_label.config(text=user_input)


button = Button(text="Click Me", command=button_clicked)
# button.pack()

#
# button.pack()
# my_label.pack()
# input.pack()






window.mainloop()






















# # Label                  Doc: https://tcl.tk/man/tcl8.6/TkCmd/pack.htm
#
# my_label = tkinter.Label(text="I am a Label", font=("Arial", 24, "bold"))
# my_label.pack()
#
# my_label["text"] = "New Text"
# my_label.config(text="New Text")
#
#
# # Part 2
# # Button
#
# def button_clicked():
#     print("I got clicked")
#     my_label.config(text="Button Got Clicked")
#
#
# button = Button(text="Click Me", command=button_clicked)
# button.pack()
#
#
#
# # Entry                  Doc: https://tcl.tk/man/tcl8.6/TkCmd/entry.htm
#
# input = Entry(width=10)
# input.pack()
# user_input = input.get()











