# Instructions

# Step 1: Create the Main Window Create a new Python file. Import Tkinter and the two file-dialog functions. Create the main window, add the title and size, and configure the row and column so the editor can expand.

# Step 2: Create the Open Function Define open_letter(). Use askopenfilename() to let the user select a text file. Add file types so the dialog clearly shows text files and other files.

# Step 3: Read the File's Contents Check whether a path was selected. Clear the Text widget, open the selected file in read mode, use read() to collect its contents, and insert the text into the editor.

# Step 4: Update the Window Title After opening the file, use window.title() with an f-string so the complete file path is displayed in the application title bar.

# Step 5: Create the Save Function Define save_letter(). Use asksaveasfilename() with a .txt default extension. Get the current text from the editor and write it to the selected file.

# Step 6: Create the Editor and Button Frame Create a Text widget for writing letters and a Frame widget to hold the Open Letter and Save Letter As buttons.

# Step 7: Pass Functions as Button Commands Set command=open_letter and command=save_letter. Do not add parentheses because Tkinter must call each function only when its button is clicked.

# Step 8: Arrange Widgets with Grid Place the buttons inside the frame, then place the frame in column 0 and the text editor in column 1. Use sticky values so the widgets stretch in the required directions.

# Step 9: Run and Test the Application Run the program, open a saved letter, edit its text, and save it with a new filename. Check that the title bar shows the correct path after both actions.


# Letter Writing Application
 
# Import the required packages
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename
 
# PART 1: Set up the main window
window = Tk()
window.title("Letter Writing Application")
window.geometry("600x500")
window.rowconfigure(0, minsize=500, weight=1)
window.columnconfigure(1, minsize=500, weight=1)
 
# PART 2: Open an existing letter
def open_letter():
    """Open a saved letter for editing."""
    filepath = askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
 
    # Stop if no file is selected
    if not filepath:
        return
 
    # Clear the editor before displaying the selected letter
    txt_edit.delete(1.0, END)
 
    # Read the file and show its contents in the editor
    with open(filepath, "r") as input_file:
        letter_text = input_file.read()
        txt_edit.insert(END, letter_text)
 
    # Show the opened file path in the window title
    window.title(f"Letter Writing Application - {filepath}")
 
# PART 3: Save the current letter
def save_letter():
    """Save the letter as a text file."""
    filepath = asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
    )
 
    # Stop if no save location is selected
    if not filepath:
        return
 
    # Get the editor text and write it to the selected file
    with open(filepath, "w") as output_file:
        letter_text = txt_edit.get(1.0, END)
        output_file.write(letter_text)
 
    # Show the saved file path in the window title
    window.title(f"Letter Writing Application - {filepath}")
 
# PART 4: Create the application widgets
txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
 
# Pass functions as button commands without parentheses
btn_open = Button(
    fr_buttons,
    text="Open Letter",
    command=open_letter
)
btn_save = Button(
    fr_buttons,
    text="Save Letter As...",
    command=save_letter
)
 
# PART 5: Arrange the widgets using the grid layout
btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)
fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")
 
# Start the Tkinter event loop
window.mainloop()
