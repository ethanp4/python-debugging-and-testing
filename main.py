class Order:
    def __init__(self, customer_name, items):
        self.customer_name = customer_name
        self.items = items  
 
    def calculate_total(self):
        total = 0
        for item in self.items:
            total += item[1] * item[2]  #logic error: quantity * price Logic error fixed '+' to '*'
        return total
 
    def add_item(self, item_name, quantity, price):
        self.items.append((item_name, quantity, price))  
 
    def remove_item(self, item_name):
        self.items = [item for item in self.items if item[0] != item_name]
 
    def print_summary(self):
        print("Order Summary for", self.customer_name)
        for item in self.items: #runtime error fixed 'itemz' to 'items'
            print(f"{item[1]} x {item[0]} @ ${item[2]:.2f}")
        print("Total: $", self.calculate_total()) #syntax error fixed: added closing parenthesis
 
    def apply_discount(self, code):
        discounts = {
            "SAVE10": 0.10,
            "SAVE20": 0.20,
            "SAVE30": 0.30 #Logical error fixed: added missing discount code
        }
        return discounts.get(code, 0.0)
 
def main():
    order = Order("Alice", [("Book", 2, 15.00), ("Pen", 5, 1.50)])
    order.add_item("Notebook", 3, 5.00)
    order.remove_item("Pen")
    order.print_summary()
 
    discount = order.apply_discount("SAVE30")
    total = order.calculate_total()
    total_after_discount = total * (1 - discount)
    print(f"Discount applied: {discount*100:.0f}%")
    print(f"Total after discount: ${total_after_discount:.2f}")

if __name__ == "__main__":
    main()