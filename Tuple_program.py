items = ("Apple", "Banana", "Grapes", "Apple", "Mango", "Papaya","Banana","Pomogranat")

print(f"Total number of items: {len(items)}")


print("1. Show All Items")
print("2. Search for an Item")
print("3. Count an Item")
print("4. Find Index of an Item")
print("5. Exit")

choice = int(input("Enter your choice: "))
if choice == 1:
     print("Items: " + ", ".join(items) + ".")

elif choice == 2:
     item_to_search = input("Enter item to search: ").lower()
     if item_to_search in [i.lower() for i in items]:
          print(f"{item_to_search} in item list.")
     else:
          print(f"{item_to_search} is not in item list.")

elif choice == 3:
     item_to_count = input("Enter item to count: ").lower()
     item_count = 0
     for item in items:
         if item == item_to_count.lower():
                item_count += 1
         else:
              print(f"{item_to_count} is not in items list")
              break
     print(f"{item_to_count} count is {item_count}")

elif choice == 4:
     lower_items = tuple(i.lower() for i in items)
     item_index = input("Enter item to find it's index: ").lower()
     print(f"Index of {item_index} is {lower_items.index(item_index)}")

elif choice == 5:
     pass

else:
     print("Enter a valid choice..")



    
          


    