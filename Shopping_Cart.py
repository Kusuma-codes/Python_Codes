class ShoppingCart:
    def __init__(self, items):
        self.items = items
    
    def add_items(self, item):
        self.items.append(item)

    def view_cart(self):
        print(f"Items in your cart: {", ".join(self.items)}")
    
    def empty_cart(self):
        self.items.clear()
    
    def remove_item(self, item1):
        if item1 in self.items:
            self.items.remove(item1)
        else:
            print("Item not found")
        
i1 = ShoppingCart(["Clibs","Hairpin","Blush","Juice"])
i1.view_cart()
i1.remove_item("Juice")
i1.empty_cart()
i1.view_cart()
i1.add_items("Clothes")
i1.add_items("Shoes")
i1.add_items("Bag")
i1.add_items("Watch")
i1.view_cart()
i1.add_items("Sunscreen")
i1.view_cart()


        
        

        