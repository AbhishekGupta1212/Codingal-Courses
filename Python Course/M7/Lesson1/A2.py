# You build a small form that greets you by name and shows today's date, using a Label, an Entry, a Text box, and a Button all working together.

# HOW IT WORKS

# Step 1: Import everything from tkinter, and also import date from datetime to display today's date.

# Step 2: Create the main window using root = Tk(), then set its title and size with root.title(...) and root.geometry(...).

# Step 3: Create a Label lbl with the text "Hey There!" and its own foreground color, background color, height, and width.

# Step 4: Create a Label name_lbl asking the user for their full name.

# Step 5: Create an Entry widget name_entry as a text box for the user to type their name into.

# Step 6: Define a function display() that reads name_entry.get(), builds a greeting and welcome message, and uses a global variable named message.

# Step 7: Inside display(), insert the greeting, message, and today's date into the text box using text_box.insert(END, ...).

# Step 8: Create a Text widget text_box to display the output messages.

# Step 9: Create a Button widget btn with the text "Begin" and command=display, so clicking it calls the display() function.

# Step 10: Arrange every widget in the window - lbl, name_lbl, name_entry, btn, and text_box - using pack().

# Step 11: Start the GUI event loop using root.mainloop(), so the window stays open and responds to user actions.


# Import necessary libraries
from tkinter import *
from datetime import date

# Create Window
root = Tk()
root.title('Getting Started with Widgets')
root.geometry('400x300')

# Add widgets
# Add Label 
lbl = Label(text="Hey There!", fg="white", bg="#072F5F", height=1, width=300)

# Add Label for getting name as input from user
# Use Entry Widget to create a text box for user to enter details
name_lbl = Label(text="Full Name", bg="#3895D3")
name_entry = Entry()

# Function to display a Message
def display():
	# Read input given by user
	name = name_entry.get()
	# Declaring a global variable 
	# to make it accessible anywhere in the program
	global message
	message = "Welcome to the Application made using tkinter! \nToday's date is: "
	greet = "Hello "+name+"\n"
	# Display details in a text box
	# Specify where to add the details inside the text box
	text_box.insert(END, greet)
	text_box.insert(END, message)
	text_box.insert(END, date.today())

# Add a Text Widget to display information/messages
text_box = Text(height=3)

# Add button and give value of command as name of the function
# Press button, display function will be called automatically
btn = Button(text="Begin", command=display, height=1, bg="#1261A0", fg='white')

# Organize all the widgets in the window
lbl.pack()
name_lbl.pack()
name_entry.pack()
btn.pack()
text_box.pack()

# Start the GUI event loop
root.mainloop()