# You build a small window with a Scan for Virus button that, when clicked, pops open a warning message box announcing that a virus has been found.

# HOW IT WORKS

# Step 1: Import everything from tkinter, and also import messagebox from tkinter to show popup alert messages.

# Step 2: Create the main window using root = Tk().

# Step 3: Set the window size using root.geometry("200x200").

# Step 4: Define a function msg() that calls messagebox.showwarning("Alert", "Stop! Virus Found.") to show a warning message box with a title and message; this function will run when the button is clicked.

# Step 5: Create a Button widget with the text "Scan for Virus" and command=msg, so clicking the button calls the msg() function.

# Step 6: Place the button on the window using button.place(x=40, y=80).

# Step 7: Start the Tkinter event loop using root.mainloop(), so the window stays open and responds to user actions.


# Import necessary libraries
from tkinter import *
from tkinter import messagebox

# Setup Tkinter Window
root = Tk()
root.geometry("200x200")

# Function for Displaying Warning Message
# This will be called once the button is clicked
# messagebox.showwarning("Window Name", "Text to be displayed")
def msg():
	messagebox.showwarning("Alert", "Stop! Virus Found.")

# Adding Button Widget to Window
button = Button(root, text="Scan for Virus", command=msg)
button.place(x=40, y=80)

# Entering main event loop
root.mainloop()