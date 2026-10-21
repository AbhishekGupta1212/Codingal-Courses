# Instructions

# Step 1: Create the Main Window Create a new Python file. Import Tkinter and messagebox. Create the main window, set its title, and choose a suitable window size.

# Step 2: Add the Heading and Instructions Create Label widgets for the app heading and the instruction that asks you to enter your next after-school task.

# Step 3: Create the Entry and Key Label Add an Entry widget for the routine task. Add another Label widget that will display the last character you typed.

# Step 4: Bind a Keypress Event Define handle_keypress(event). Use event.char to read the typed character, then update key_label. Bind the Entry widget to the <Key> event using .bind().

# Step 5: Bind a Mouse-Click Event Define handle_click(event). Create the routine message label and bind its left mouse click to <Button-1>. When the label is clicked, update its text.

# Step 6: Create the Routine-Checking Function Define check_routine(). Read the text from task_entry using get(). If the entry is empty, display a warning popup using messagebox.showwarning().

# Step 7: Connect the Button Command Create the Check My Routine button and set command=check_routine. Do not add parentheses because Tkinter should call the function only when the button is pressed.

# Step 8: Run and Test the Application Run the program. Type a task to test the keypress event, click the routine area to test the mouse event, and press the button with both an empty and completed entry box.

# After-School Routine Checker
# Import the required packages
from tkinter import *
from tkinter import messagebox
 
# PART 1: Create the main window
window = Tk()
window.title("After-School Routine Checker")
window.geometry("400x320")
 
# PART 2: Add the heading and instructions
heading = Label(
    window,
    text="My After-School Routine",
    font=("Arial", 16, "bold")
)
heading.pack(pady=10)
 
instruction = Label(
    window,
    text="Enter your next after-school task:"
)
instruction.pack()
 
# PART 3: Create the task entry box
task_entry = Entry(window, width=35)
task_entry.pack(pady=8)
 
# Label used to display the last key pressed
key_label = Label(window, text="Last key pressed: None")
key_label.pack(pady=5)
 
# PART 4: Handle a keypress event
def handle_keypress(event):
    """Display the character associated with the key pressed."""
    key_label.config(text="Last key pressed: " + event.char)
 
# Bind keypress events to the Entry widget
task_entry.bind("<Key>", handle_keypress)
 
# PART 5: Handle a mouse-click event
def handle_click(event):
    """Update the message when the routine area is clicked."""
    routine_message.config(text="Routine area selected!")
 
routine_message = Label(
    window,
    text="Click here to check your routine",
    bg="#d0efff",
    width=32,
    height=3
)
routine_message.pack(pady=10)
 
# Bind the left mouse button to the event handler
routine_message.bind("<Button-1>", handle_click)
 
# PART 6: Check the entered routine task
def check_routine():
    """Display the task or show a warning when it is missing."""
    task = task_entry.get()
 
    if task == "":
        messagebox.showwarning(
            "Missing Task",
            "Please enter an after-school task."
        )
    else:
        routine_message.config(text="Next task: " + task)
 
# PART 7: Connect the button command to the function
check_button = Button(
    window,
    text="Check My Routine",
    command=check_routine
)
check_button.pack(pady=10)
 
# Start the Tkinter event loop
window.mainloop()
