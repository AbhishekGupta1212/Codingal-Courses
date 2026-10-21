# You build a registration form with name, email, and password fields, a Create Account button, and a text box that displays a personalized greeting.

# HOW IT WORKS

# Step 1: Import everything from tkinter and create the main window with a title and 400x400 size.

# Step 2: Create a Frame to organize the form, and three Labels for Full Name, Email Id, and Enter Password.

# Step 3: Create three Entry widgets - name_entry, email_entry, and pass_entry with show="*" for the hidden password.

# Step 4: Define display(): read name_entry.get(), build a greeting message, and insert it into a Text widget named textbox.

# Step 5: Create the textbox itself and a Button labeled "Create Account" with command=display.

# Step 6: Place every widget - the frame, labels, entries, button, and textbox - at its own exact x, y position.

# Step 7: Call root.mainloop() to keep the login window open and responsive.


# Import necessary libraries
from tkinter import *

# Create Window
root = Tk()
root.title('Login App')
root.geometry('400x400')

# Create a frame to organize elements better
frame = Frame(master=root, height=200, width=360, bg="#d0efff")

# Add widgets
# Add Label 
name_lbl = Label(frame, text = "Full Name", bg="#3895D3", fg='white', width=12)
email_lbl = Label(frame, text = "Email Id", bg="#3895D3", fg='white', width=12)
password_lbl = Label(frame, text = "Enter Password", bg="#3895D3", fg='white', width=12)

# Use Entry Widget to create a text box for user to enter details
name_entry = Entry(frame)
email_entry = Entry(frame)
pass_entry = Entry(frame, show="*")

# Function to display message
def display():
	name = name_entry.get()
	greet = "Hey "+name
	message =  "\nCongratulations for your new account!"
	textbox.insert(END, greet)
	textbox.insert(END, message)

# Textbox to display message
textbox = Text(bg="#BEBEBE", fg="black")

# Add Button, when pressed, message will be displayed
btn = Button(text = "Create Account", command=display, bg="red")

# Arrange all widgets
frame.place(x=20,y=0)
name_lbl.place(x=20, y=20)
name_entry.place(x=150, y=20)
email_lbl.place(x=20, y=80)
email_entry.place(x=150, y=80)
password_lbl.place(x=20, y=140)
pass_entry.place(x=150, y=140)
btn.place(x=130, y=210)
textbox.place(y=250)

# Start the GUI event loop
root.mainloop()