# Step 1: Import the Libraries Create a new Python file. Import Tkinter using from tkinter import * and import date from the datetime module.

# Step 2: Create the Main Window Use Tk() to create the application window. Set a clear title and geometry so the interface has enough space.

# Step 3: Add the Heading Label Create a Label widget that displays Workshop Welcome Desk. Use foreground and background colours to make the heading easy to notice.

# Step 4: Add the Name Input Create another Label for Participant Name and an Entry widget where the participant can type their name.

# Step 5: Create the Display Function Define display_welcome(). Use name_entry.get() to read the typed name, then prepare a greeting, welcome line, and current date.

# Step 6: Display Multi-Line Output Create a Text widget. Inside the function, clear any previous message and use text_box.insert() to add each part of the output.

# Step 7: Connect the Button Command Create a Check In button and set command=display_welcome. Do not add parentheses because Tkinter should call the function only after the button is selected.

# Step 8: Arrange the Widgets Use pack() to place the heading, participant label, Entry widget, button, and Text widget in a clear vertical layout.

# Step 9: Run and Test the Application Run the program, type a participant name, and select Check In. Confirm that the greeting, workshop message, and current date appear on separate lines.


# Workshop Participant Greeting
# Import necessary libraries
from tkinter import *
from datetime import date
 
# PART 1: Create the main window
root = Tk()
root.title("Workshop Participant Greeting")
root.geometry("400x300")
 
# PART 2: Create the heading label
heading = Label(
    text="Workshop Welcome Desk",
    fg="white",
    bg="#072F5F",
    height=1,
    width=300
)
 
# PART 3: Create a label and Entry widget
name_label = Label(
    text="Participant Name",
    bg="#3895D3"
)
name_entry = Entry()
 
# PART 4: Create the display function
def display_welcome():
    # Read the participant's name from the Entry widget
    name = name_entry.get()
 
    # Clear the previous message
    text_box.delete(1.0, END)
 
    # Create the multi-line welcome message
    greeting = "Hello " + name + "!\n"
    message = "Welcome to the workshop.\n"
    workshop_date = "Date: " + str(date.today())
 
    # Insert the message into the Text widget
    text_box.insert(END, greeting)
    text_box.insert(END, message)
    text_box.insert(END, workshop_date)
 
# PART 5: Create the Text widget
text_box = Text(
    height=4,
    width=40
)
 
# PART 6: Create the button and connect its command
welcome_button = Button(
    text="Check In",
    command=display_welcome,
    height=1,
    bg="#1261A0",
    fg="white"
)
 
# PART 7: Arrange the widgets
heading.pack()
name_label.pack(pady=10)
name_entry.pack()
welcome_button.pack(pady=10)
text_box.pack()
 
# PART 8: Start the Tkinter event loop
root.mainloop()
