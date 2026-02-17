"""
INTERACTIVE GROCERY LIST MANAGER
--------------------------------
Features:
- Add items to the list
- Remove items from the list  
- View current list with numbered items
- Show total number of items
- Exit program
"""

print("==================================\n   GROCERY LIST MANAGER  \n==================================\nCommands: \n\ta - add item\n\tr - remove item\n\tv - view list\n\tc - check if item exists\n\tq - quit\n")
cart=[]
while True:
    cmd = input("So.. what would you like to do? ")
    if cmd=="a":
        item=input("Enter item to add: ")
        cart.append(item)
        print(f"'{item}' added to list!")
    elif cmd=="r":
        item=input("What do you want to remove? ")
        if item in cart:
            cart.remove(item)
            print(f"'{item}' removed!")
        else:
            print("You don't even have it!")
            print(f"{item} not removed!")
    elif cmd=="q":
        print("Have a great time! ")
        break
    elif cmd=="v":
        print(f"==================================\n ITEMS \n ==================================\n {[x for x in cart]}\n you have added {len(cart)} products to the cart!")
    elif cmd=="c":
        item = input("Item to check: ")
        if item in cart:
            print("Yes it is!")
        else:
            print("No!")
    else:
        break
        
# ): just the beginning 
    
