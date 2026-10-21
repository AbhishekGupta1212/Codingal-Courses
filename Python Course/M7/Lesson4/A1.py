# You build a working text editor with Open and Save As buttons, able to load any text file, edit it, and save your changes back to disk.

# HOW IT WORKS

# Step 1: Import everything from tkinter, plus askopenfilename and asksaveasfilename from tkinter.filedialog.

# Step 2: Create the main window with Tk(), set its title and 600x500 size, and configure the grid to expand.

# Step 3: Define open_file(): call askopenfilename() to choose a file, returning early if nothing was chosen.

# Step 4: Inside open_file(), clear the editor with delete(1.0, END), read the file, then insert its text with insert(END, text).

# Step 5: Update the window's title to show the newly opened file's path.

# Step 6: Define save_file(): call asksaveasfilename() to choose a save location, returning early if nothing was chosen.

# Step 7: Inside save_file(), get the editor's current text with get(1.0, END), then write it to the chosen file.

# Step 8: Update the window's title again to show the newly saved file's path.

# Step 9: Create the Text widget, the button frame, and an Open and a Save As button, wiring each button's command to its matching function.

# Step 10: Arrange everything with grid(), then call window.mainloop() to start the application.

# Import necessary packages 
from tkinter import *
from tkinter.filedialog import askopenfilename, asksaveasfilename

# Setup Root Window
window = Tk()
window.title("Text Editor")
window.geometry("600x500")
window.rowconfigure(0, minsize=800, weight=1)
window.columnconfigure(1, minsize=800, weight=1)

# Function to Open a file
def open_file():
	"""Open a file."""
	filepath = askopenfilename(
		filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
	)
	if not filepath:
		return
	txt_edit.delete(1.0, END)
	# if a file is opened then display the contents of the file
	with open(filepath, "r") as input_file:
		# Read contents of the input file
		text = input_file.read()
		# Insert contents of the file in the editor box
		txt_edit.insert(END, text)
		input_file.close()
	window.title(f"Text Editor - {filepath}")

# Function to Save a file
def save_file():
	# Save the current file as a new file
	filepath = asksaveasfilename(
		defaultextension="txt",
		filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
	)
	if not filepath:
		return
	with open(filepath, "w") as output_file:
		# Read the edited content and update in the output file
		text = txt_edit.get(1.0, END)
		output_file.write(text)
	window.title(f"Text Editor - {filepath}")

# Add widgets in the application
txt_edit = Text(window)
fr_buttons = Frame(window, relief=RAISED, bd=2)
btn_open = Button(fr_buttons, text="Open", command=open_file)
btn_save = Button(fr_buttons, text="Save As...", command=save_file)

btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
btn_save.grid(row=1, column=0, sticky="ew", padx=5)

fr_buttons.grid(row=0, column=0, sticky="ns")
txt_edit.grid(row=0, column=1, sticky="nsew")

# Start the GUI event loop
window.mainloop()