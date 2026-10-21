# You build the simplest possible Tkinter window - just a titled, sized window with nothing inside it yet.

# HOW IT WORKS

# Step 1: Import everything from tkinter to create the GUI.

# Step 2: Create the main window using window = Tk().

# Step 3: Set the window's title using window.title('Demo Window').

# Step 4: Set the window's size using window.geometry('400x300').

# Step 5: Start the GUI event loop using window.mainloop(), so the window stays open.

# Import necessary libraries
from tkinter import *

# Create Window
window = Tk()

# Set the window Title and Geometry
window.title('Demo')
window.geometry('400x300')

# Start the GUI event loop
window.mainloop()

