class Cart:
    def __init__(self):
        self.items = {}
    
    def add_items(self, item, price):
        self.items[item] = price
    
    def total_price(self):
        total_sum = sum(self.items.values())
        return f"Total price: {total_sum}"
    
    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
            print(f"{item} removed from list")
        else:
            print(f"{item} is not in the list")

    def view_cart(self):
        if not self.items:
            print("Your cart is empty")
        else:
            print("items in Cart: ")
            for item, price in self.items.items():
                print(f"{item} - {price}")
            
    def total_price(self):
        total_sum = sum(self.items.values())
        print(f"Total price: {total_sum}")
    
i1 = Cart()
i1.add_items("Book", 200)
i1.add_items("Pen", 100)
i1.add_items("Sharpner", 10)
i1.add_items("Eraser", 10)
i1.add_items("Pencil", 50)
i1.remove_item("Ink")
i1.view_cart()
i1.total_price()



    

        
        

        
        