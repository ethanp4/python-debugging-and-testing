import random
import time
import os
 
class Order:
    # Province-based tax rates (GST/HST/PST included)
    TAX_RATES = {
        "AB": 0.05, "BC": 0.12, "SK": 0.11, "MB": 0.12,
        "ON": 0.13, "QC": 0.14975, "NB": 0.15, "NS": 0.15,
        "PE": 0.15, "NL": 0.15, "NT": 0.05, "NU": 0.05, "YT": 0.05
    }
 
    # Neon / bright color codes
    COLORS = [
        #"\033[95m",  # Bright Magenta
        "\033[94m",  # Bright Blue
        #"\033[96m",  # Bright Cyan
        "\033[92m",  # Bright Green
        #"\033[93m",  # Bright Yellow
        "\033[91m",  # Bright Red
        "\033[97m",  # Bright White
        #"\033[38;5;206m",  # Neon Pink
        #"\033[38;5;51m",   # Neon Aqua
        #"\033[38;5;118m",  # Neon Lime
        #"\033[38;5;214m",  # Neon Orange
    ]
 
    def __init__(self, customer_name, items, province="AB"):
        self.customer_name = customer_name
        self.items = items
        self.province = province if province in self.TAX_RATES else "AB"
 
    def colorize(self, text):
        """Gives each character a random neon color."""
        return ''.join(random.choice(self.COLORS) + ch for ch in text)
 
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1] * item[2]
        return total
 
    def add_item(self, item_name, quantity, price):
        self.items.append((item_name, quantity, price))
 
    def remove_item(self, item_name):
        self.items = [item for item in self.items if item[0] != item_name]
 
    def print_summary(self):
        print(self.colorize(f"Order Summary for {self.customer_name} ({self.province})"))
        for item in self.items:
            print(self.colorize(f"{item[1]} x {item[0]} @ ${item[2]:.2f}"))
        subtotal = self.calculate_total()
        tax_rate = self.TAX_RATES.get(self.province, self.TAX_RATES["AB"])
        tax = subtotal * tax_rate
        total_with_tax = subtotal + tax
        print(self.colorize(f"Subtotal: ${subtotal:.2f}"))
        print(self.colorize(f"Tax ({tax_rate*100:.2f}%): ${tax:.2f}"))
        print(self.colorize(f"Total (after tax): ${total_with_tax:.2f}"))
 
    def apply_discount(self, code):
        discounts = {
            "SAVE10": 0.10,
            "SAVE20": 0.20,
            "SAVE30": 0.30
        }
        return discounts.get(code, 0.0)
 
 
def main():
    # Create the order (default province = AB)
    order = Order("Alice", [("Book", 2, 15.00), ("Pen", 5, 1.50)])
    order.add_item("Notebook", 3, 5.00)
    order.remove_item("Pen")
 
    discount = order.apply_discount("SAVE30")
    total = order.calculate_total()
    total_after_discount = total * (1 - discount)
    tax_rate = order.TAX_RATES.get(order.province, 0.05)
    total_after_tax = total_after_discount * (1 + tax_rate)
 
    while True:
        # Clear the screen (works on Windows/macOS/Linux)
        os.system('cls' if os.name == 'nt' else 'clear')
 
        # Print the neon order summary
        order.print_summary()
        print()
        print(order.colorize(f"Discount applied: {discount*100:.0f}%"))
        print(order.colorize(f"Total after discount: ${total_after_discount:.2f}"))
        print(order.colorize(f"Total after discount and tax: ${total_after_tax:.2f}"))
 
        # Delay before looping again (1 second)
        time.sleep(0.9)
 
if __name__ == "__main__":
    main()
 