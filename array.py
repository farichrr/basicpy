stuff = []

def displayItem(inventory):
    print("Inventory list : ")
    item_total = 0
    for item, quantity in inventory.items():
        print(str(quantity)+'    '+item)
        item_total += quantity
    
    print("Total Number items: " + str(item_total))

displayItem(stuff)
