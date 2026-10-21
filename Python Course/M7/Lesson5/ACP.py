# Instructions

# Step 1: Create the Main Window Create a new Python file and import Tkinter and messagebox. Create the root window, then set its title, size, and background.

# Step 2: Add the Main-Window Widgets Add a heading, a short instruction, and a button. The button will open the reading-plan window.

# Step 3: Create the Toplevel Window Define topwin(). Inside it, create Toplevel(root) and configure the new window's title, geometry, and background.

# Step 4: Add Inputs and Results Inside the Toplevel window, create Entry widgets for total pages and pages per day. Add two more Entry widgets for complete days and remaining pages.

# Step 5: Define the Nested Function Inside topwin(), define calculate_plan(). This function can directly use the Entry widgets created in the same outer function.

# Step 6: Read and Validate the Input Use .get() to read both entries and int() to convert the text to whole numbers. Check that both values are greater than zero.

# Step 7: Calculate the Reading Schedule Use // to find the number of complete reading days. Use % to find the number of pages remaining after those complete days.

# Step 8: Display the Results Clear the result entries with delete(), then display the calculated values using insert().

# Step 9: Handle Invalid Input Place the input conversion and calculations inside try. Use except ValueError to display an error if the user enters text or another invalid value.

# Step 10: Run and Test the Application Run the program, open the reading-plan window, and test it with different page totals and daily targets. Also test blank, text, zero, and negative inputs.


# Reading Schedule Planner
# Import necessary libraries
from tkinter import *
from tkinter import messagebox
 
# PART 1: Set up the main window
root = Tk()
root.title("Reading Schedule Planner")
root.configure(bg="light blue")
root.geometry("500x300")
 
# Add heading and instruction labels
heading = Label(
    root,
    text="Reading Schedule Planner",
    font=("Arial", 18, "bold"),
    bg="light blue"
)
heading.pack(pady=50)
 
instruction = Label(
    root,
    text="Create a simple plan to complete your book.",
    bg="light blue"
)
instruction.pack(pady=10)
 
# PART 2: Open the Toplevel window
def topwin():
    # Create and configure the Toplevel window
    top = Toplevel(root)
    top.title("Create Reading Plan")
    top.configure(bg="light grey")
    top.geometry("500x350+50+50")
 
    # Add labels and input fields
    pages_label = Label(
        top,
        text="Enter total number of pages:",
        bg="light grey"
    )
    pages_entry = Entry(top)
 
    daily_label = Label(
        top,
        text="Enter pages you can read each day:",
        bg="light grey"
    )
    daily_entry = Entry(top)
 
    result_label = Label(
        top,
        text="Your Reading Plan",
        font=("Arial", 14, "bold"),
        bg="light grey"
    )
 
    days_label = Label(
        top,
        text="Complete reading days:",
        bg="light grey"
    )
 
    remaining_label = Label(
        top,
        text="Pages remaining:",
        bg="light grey"
    )
 
    days_entry = Entry(top)
    remaining_entry = Entry(top)
 
    # PART 3: Define a function inside topwin()
    def calculate_plan():
        try:
            # Read and convert the input values
            total_pages = int(pages_entry.get())
            pages_per_day = int(daily_entry.get())
 
            # Check that both values are greater than zero
            if total_pages <= 0 or pages_per_day <= 0:
                messagebox.showerror(
                    "Invalid Input",
                    "Please enter numbers greater than zero."
                )
                return
 
            # PART 4: Use floor division and modulo
            complete_days = total_pages // pages_per_day
            remaining_pages = total_pages % pages_per_day
 
            # Clear previous results
            days_entry.delete(0, END)
            remaining_entry.delete(0, END)
 
            # Display the results
            days_entry.insert(END, str(complete_days))
            remaining_entry.insert(END, str(remaining_pages))
 
        # PART 5: Handle invalid input
        except ValueError:
            messagebox.showerror(
                "Invalid Input",
                "Please enter valid whole numbers."
            )
 
    # Add button connected to the nested function
    calculate_button = Button(
        top,
        text="Create Plan",
        command=calculate_plan,
        bg="#1261A0",
        fg="white"
    )
 
    # Position widgets in the Toplevel window
    pages_label.place(x=80, y=40)
    pages_entry.place(x=280, y=40)
 
    daily_label.place(x=80, y=90)
    daily_entry.place(x=280, y=90)
 
    calculate_button.place(x=205, y=135)
    result_label.place(x=175, y=185)
 
    days_label.place(x=80, y=235)
    days_entry.place(x=280, y=235)
 
    remaining_label.place(x=80, y=275)
    remaining_entry.place(x=280, y=275)
 
# Add button to open the Toplevel window
start_button = Button(
    root,
    text="Create My Reading Plan",
    command=topwin,
    bg="#1261A0",
    fg="white"
)
start_button.pack(pady=15)
 
# Start the main Tkinter event loop
root.mainloop()
