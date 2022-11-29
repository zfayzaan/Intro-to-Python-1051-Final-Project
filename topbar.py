from tkinter import*

root =Tk()


my_menu= Menu(root)
root.config(menu=my_menu)

#Creating the menu items

file_menu = Menu(my_menu)
my_menu.add_cascade(label="Main Menu",menu=file_menu)
file_menu.add_command(Label="New.." , commmand=our_command)


root.mainloop()
