# Instructions

# Step 1: Prepare the Project Files Create a new Python file and save it in a project folder. Add a PNG image named background.png to the same folder.

# Step 2: Import Tkinter and ttk Import tkinter as tk. Import ttk and messagebox so you can use themed widgets and popup messages.

# Step 3: Create the Application Class Define the StationeryOrderManagement class. Inside __init__(), store the root window and set its title.

# Step 4: Store the Stationery Data Create a dictionary containing the stationery item names and prices. Also create the exchange_rate variable.

# Step 5: Draw the Canvas Background Define setup_background(). Create a Canvas, load background.png with PhotoImage, and display it using create_image().

# Step 6: Build the Interface with ttk Widgets Create a ttk.Frame and add themed labels, entries, a combobox, and a button. Use grid() to arrange the widgets.

# Step 7: Create Rows with enumerate() Loop through the stationery dictionary with enumerate(..., start=1). Use the index as the grid row for each item.

# Step 8: Update Prices with Ternary Expressions In update_item_prices(), use ternary expressions to choose the currency symbol and conversion rate.

# Step 9: Validate Quantities with .isdigit() In place_order(), read each Entry value and use .isdigit() before converting it to an integer.

# Step 10: Run and Test the Application Run the program, enter quantities, switch currencies, and place an order. Check that the summary and total are correct.


# Stationery Order Management App
 
# Import tkinter for GUI and ttk for improved widgets
import tkinter as tk
from tkinter import ttk, messagebox
import os
from PIL import Image, ImageTk
 
# Define the StationeryOrderManagement class
class StationeryOrderManagement:
 
    # Initialize the application
    def __init__(self, root):
        self.root = root
        self.root.title("Stationery Order Management App")
 
        # Store stationery items and their prices
        self.stationery_items = {
            "NOTEBOOK": 3,
            "PENCIL PACK": 2,
            "PEN SET": 4,
            "ERASER": 1,
            "GEOMETRY BOX": 6,
            "COLOUR PENCILS": 5
        }
 
        # Exchange rate for currency conversion
        self.exchange_rate = 82
 
        # Set up the Canvas background
        self.setup_background(root)
 
        # Create a themed frame to hold the widgets
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)
 
        # Heading label
        ttk.Label(
            frame,
            text="Stationery Order Management",
            font=("Arial", 20, "bold")
        ).grid(
            row=0,
            columnspan=3,
            padx=10,
            pady=10
        )
 
        # Store references to labels and Entry widgets
        self.item_labels = {}
        self.item_quantities = {}
 
        # Create one row for every stationery item
        for index, (item, price) in enumerate(
            self.stationery_items.items(),
            start=1
        ):
            item_label = ttk.Label(
                frame,
                text=f"{item} (${price}):",
                font=("Arial", 12)
            )
 
            item_label.grid(
                row=index,
                column=0,
                padx=10,
                pady=5
            )
 
            self.item_labels[item] = item_label
 
            quantity_entry = ttk.Entry(
                frame,
                width=5
            )
 
            quantity_entry.grid(
                row=index,
                column=1,
                padx=10,
                pady=5
            )
 
            self.item_quantities[item] = quantity_entry
 
        # Variable for storing the selected currency
        self.currency_var = tk.StringVar()
 
        ttk.Label(
            frame,
            text="Currency:",
            font=("Arial", 12)
        ).grid(
            row=len(self.stationery_items) + 1,
            column=0,
            padx=10,
            pady=5
        )
 
        # Currency selection dropdown
        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            state="readonly",
            width=18,
            values=("USD", "INR")
        )
 
        currency_dropdown.grid(
            row=len(self.stationery_items) + 1,
            column=1,
            padx=10,
            pady=5
        )
 
        # Select USD as the default currency
        currency_dropdown.current(0)
 
        # Update prices whenever the currency changes
        self.currency_var.trace(
            "w",
            self.update_item_prices
        )
 
        # Button to place the stationery order
        order_button = ttk.Button(
            frame,
            text="Place Order",
            command=self.place_order
        )
 
        order_button.grid(
            row=len(self.stationery_items) + 2,
            columnspan=3,
            padx=10,
            pady=10
        )
 
    # Set up the Canvas background
    def setup_background(self, root):
        bg_width, bg_height = 800, 600
        canvas = tk.Canvas(root, width=bg_width, height=bg_height)
        canvas.pack()

    # Absolute path, independent of working directory
        script_dir = os.path.dirname(os.path.abspath(__file__))
        image_path = os.path.join(script_dir, "background.png")  # or whatever file you're using

        pil_image = Image.open(image_path).resize((bg_width, bg_height))
        background_image = ImageTk.PhotoImage(pil_image)

        canvas.create_image(0, 0, anchor=tk.NW, image=background_image)
        canvas.image = background_image  # keep a reference so it isn't garbage-collected
 
    # Update item prices according to the selected currency
    def update_item_prices(self, *args):
        currency = self.currency_var.get()
 
        # Pick values using the ternary operator
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1
 
        for item, label in self.item_labels.items():
            price = self.stationery_items[item] * rate
 
            label.config(
                text=f"{item} ({symbol}{price}):"
            )
 
    # Read quantities and place the order
    def place_order(self):
        total_cost = 0
        order_summary = "Stationery Order Summary:\n"
 
        currency = self.currency_var.get()
 
        # Pick values using the ternary operator
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1
 
        for item, entry in self.item_quantities.items():
            quantity = entry.get()
 
            # Validate that the quantity contains digits
            if quantity.isdigit():
                quantity = int(quantity)
 
                price = self.stationery_items[item] * rate
                cost = quantity * price
                total_cost += cost
 
                if quantity > 0:
                    order_summary += (
                        f"{item}: {quantity} x "
                        f"{symbol}{price} = {symbol}{cost}\n"
                    )
 
        if total_cost > 0:
            order_summary += (
                f"\nTotal Cost: {symbol}{total_cost}"
            )
 
            messagebox.showinfo(
                "Order Placed",
                order_summary
            )
 
        else:
            messagebox.showerror(
                "Error",
                "Please order at least one stationery item."
            )
 
 
# Main block to run the application
if __name__ == "__main__":
    root = tk.Tk()
 
    app = StationeryOrderManagement(root)
 
    root.geometry("800x600")
 
    # Start the GUI event loop
    root.mainloop()
