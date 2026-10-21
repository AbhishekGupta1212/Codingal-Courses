# You build a restaurant ordering app with a background image, a themed menu form, a currency dropdown, and a Place Order button that totals up a validated order.

# HOW IT WORKS

# Step 1: Import tkinter as tk, and import ttk and messagebox from tkinter.

# Step 2: Define a class RestaurantOrderManagement with an __init__(self, root) method that sets up the whole app.

# Step 3: Inside __init__, set the window's title and store a menu_items dictionary mapping each item to its price, plus an exchange_rate of 82.

# Step 4: Call self.setup_background(root) to draw a background image on a Canvas before anything else is placed.

# Step 5: Create a ttk.Frame to hold all the widgets, centered in the window, with a heading Label at the top.

# Step 6: Loop over self.menu_items with enumerate(..., start=1), creating a ttk.Label and a ttk.Entry for each item's row, and storing references in menu_labels and menu_quantities.

# Step 7: Create a currency_var StringVar and a ttk.Combobox listing "USD" and "INR", then connect it with currency_var.trace("w", self.update_menu_prices) so changing it updates prices automatically.

# Step 8: Create a ttk.Button labeled "Place Order" with command=self.place_order.

# Step 9: Define setup_background(self, root): create a Canvas, load "background.png" with tk.PhotoImage(), shrink it with .subsample(), and draw it with canvas.create_image().

# Step 10: Define update_menu_prices(self, *args): pick the correct currency symbol and exchange rate with a ternary operator, then update every menu label's displayed price.

# Step 11: Define place_order(self): for each menu item, read its typed quantity and check quantity.isdigit() before converting and adding its cost to the total.

# Step 12: If the total cost is greater than 0, show the order summary with messagebox.showinfo(); otherwise show an error with messagebox.showerror().

# Step 13: In the main block, create the root window, create the app with RestaurantOrderManagement(root), set its geometry to 800x600, and start root.mainloop().

# Import tkinter for GUI and ttk for improved widgets
import tkinter as tk
from tkinter import ttk, messagebox
import os
from PIL import Image, ImageTk

# Define the RestaurantOrderManagementApp class
class RestaurantOrderManagement:
    # Initialize the application
    def __init__(self, root):
        self.root = root  # The main window of the app
        self.root.title("Restaurant Management App")  # Set the title of the window

        # A dictionary to store the menu items and their prices
        self.menu_items = {
            "FRIES MEAL": 2,
            "LUNCH MEAL": 2,
            "BURGER MEAL": 3,
            "PIZZA MEAL": 4,
            "CHEESE BURGER": 2.5,
            "DRINKS": 1
        }

        self.exchange_rate = 82  # Exchange rate for currency conversion

        self.setup_background(root)  # Set up the background image

        # Create a frame to hold the widgets
        frame = ttk.Frame(root)
        frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        # Heading label
        ttk.Label(
            frame,
            text="Restaurant Order Management",
            font=("Arial", 20, "bold")
        ).grid(row=0, columnspan=3, padx=10, pady=10)

        self.menu_labels = {}       # To store references to menu item labels
        self.menu_quantities = {}   # To store references to quantity entry widgets

        # Create labels and entry widgets for each menu item
        for i, (item, price) in enumerate(self.menu_items.items(), start=1):
            label = ttk.Label(
                frame,
                text=f"{item} (${price}):",
                font=("Arial", 12)
            )
            label.grid(row=i, column=0, padx=10, pady=5)
            self.menu_labels[item] = label

            quantity_entry = ttk.Entry(frame, width=5)
            quantity_entry.grid(row=i, column=1, padx=10, pady=5)
            self.menu_quantities[item] = quantity_entry

        # Currency selection
        self.currency_var = tk.StringVar()
        ttk.Label(
            frame,
            text="Currency:",
            font=("Arial", 12)
        ).grid(
            row=len(self.menu_items) + 1,
            column=0,
            padx=10,
            pady=5
        )

        # Dropdown for currency selection
        currency_dropdown = ttk.Combobox(
            frame,
            textvariable=self.currency_var,
            state="readonly",
            width=18,
            values=("USD", "INR")
        )
        currency_dropdown.grid(
            row=len(self.menu_items) + 1,
            column=1,
            padx=10,
            pady=5
        )
        currency_dropdown.current(0)  # Set default currency
        self.currency_var.trace("w", self.update_menu_prices)

        # Button to place the order
        order_button = ttk.Button(
            frame,
            text="Place Order",
            command=self.place_order
        )
        order_button.grid(
            row=len(self.menu_items) + 2,
            columnspan=3,
            padx=10,
            pady=10
        )

    # Method to set up the background image

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

    # Method to update the menu prices based on the selected currency
    def update_menu_prices(self, *args):
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1

        for item, label in self.menu_labels.items():
            price = self.menu_items[item] * rate
            label.config(text=f"{item} ({symbol}{price}):")

    # Method to place an order
    def place_order(self):
        total_cost = 0
        order_summary = "Order Summary:\n"
        currency = self.currency_var.get()
        symbol = "₹" if currency == "INR" else "$"
        rate = self.exchange_rate if currency == "INR" else 1

        for item, entry in self.menu_quantities.items():
            quantity = entry.get()
            if quantity.isdigit():
                quantity = int(quantity)
                price = self.menu_items[item] * rate
                cost = quantity * price
                total_cost += cost

                if quantity > 0:
                    order_summary += (
                        f"{item}: {quantity} x {symbol}{price} = {symbol}{cost}\n"
                    )

        if total_cost > 0:
            order_summary += f"\nTotal Cost: {symbol}{total_cost}"
            messagebox.showinfo("Order Placed", order_summary)
        else:
            messagebox.showerror("Error", "Please order at least one item.")

# Main block to run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = RestaurantOrderManagement(root)
    root.geometry("800x600")  # Set the size of the window
    root.mainloop()           # Start the GUI loop
