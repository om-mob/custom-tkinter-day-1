## Simple graphical user interface for a login system
## Youtube Video URL: https://www.youtube.com/watch?v=iM3kjbbKHQU
## Youtube video Title:  Modern Graphical User Interfaces in Python - NeuralNine (12m)

import customtkinter ## CTk(), CTkFrame(), CTkLabel(), CTkEntry(), CTkButton(), CTkCheckBox()

## General Settings
customtkinter.set_appearance_mode("dark") ## System (default), dark, light
customtkinter.set_default_color_theme("blue") ## Themes: blue (default), green, dark-blue

## Initialize the root element
root = customtkinter.CTk() ## create CTk window
root.geometry("500x350")

## Implement the login logic
def login():
    """Should implement the login logic
    """
    print("test")


## Create a frame, that contains all the interface elements
frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True) ## You can also Use: frame.grid()

## Add a label (title) for your application
label = customtkinter.CTkLabel(master=frame, text="Login System", text_font=("Roboto", 24))
label.pack(pady=12, padx=10)

## Add 2 Entries for username and password
entry1 = customtkinter.CTkEntry(master=frame, placeholder_text="Username")
entry1.pack(pady=12, padx=10)
entry2 = customtkinter.CTkEntry(master=frame, placeholder_text="Password", show="*")
entry2.pack(pady=12, padx=10)

## add a button
button = customtkinter.CTkButton(master=frame, text="Login", command=login)
button.pack(pady=12, padx=10)

## add a check box
checkbox = customtkinter.CTkCheckBox(master=frame, text="Remember Me")
checkbox.pack(pady=12, padx=10)

## Run the the main loop of the program
root.mainloop()



### NOTE ###
## Every Component needs to be packed (rendered) on the window. (using the 'pack' method)
## So not only you create the component, you also need to explicitly render it

## Each Component needs a master. So when calling the CTK...() constructor, The first argument is always the master
## Most Components has the master of frame