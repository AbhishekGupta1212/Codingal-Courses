# You build a phone-style number pad with 12 bordered cells arranged into 4 rows and 3 columns, each showing its own number or symbol.

# HOW IT WORKS

# Step 1: Import everything from tkinter and create the main window with a title and 250x300 size.

# Step 2: Store the keypad's numbers and symbols in a 2D list named nums, one inner list per row.

# Step 3: Start an outer loop with i from 0 to 3, one pass per row.

# Step 4: Configure that row's column and row sizing with columnconfigure() and rowconfigure() so cells resize evenly.

# Step 5: Start an inner loop with j from 0 to 2, one pass per column.

# Step 6: Create a Frame with relief=SUNKEN and borderwidth=1, then place it with frame.grid(row=i, column=j).

# Step 7: Create a Label inside that frame showing nums[i][j], then pack() it with padding.

# Step 8: Call root.mainloop() to keep the keypad window open.


# Import necessary libraries
from tkinter import *

# Create Window
root = Tk()
root.title('Phone-Style Dial Pad')
root.geometry('250x300')

# Create a frame to organize elements better
# frame = Frame(master=root, height=200, width=360, bg="#d0efff")

nums = [[9, 8, 7], [6, 5, 4], [3, 2, 1], ['#', 0, '*']]

for i in range(4):
	# Configure rows and columns to resize window
	root.columnconfigure(i, weight=1, minsize=75)
	root.rowconfigure(i, weight=1, minsize=50)
	for j in range(0, 3):
		frame = Frame(
			master=root,
			relief=SUNKEN,
			borderwidth=1
		)
		frame.grid(row=i, column=j)
		label = Label(master=frame, text=nums[i][j], bg='#d0efff')
		label.pack(padx=3, pady=3)

# Start the GUI event loop
root.mainloop()