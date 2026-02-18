# Create a phonebook dictionary with ad-
# d/lookup/delete.

phonebook = {}
print("===================\n The Phonebook     \n===================\n\ta - add\n\tl - lookup\n\td - delete\n\tq - quit\n\tc - List contact")
while True:
    cmd = input("Enter your command here: ").lower()
    if cmd=="a":
        name = input("Enter the name: ").lower()
        phone = input("Enter the phone number: ")
        phonebook[name]=phone
    elif cmd=="l":
        name = input("Enter to search for: ").lower()
        if name in phonebook:
            print(f"Here is {name.title()}'s phone:",phonebook[name])
        else:
            print(f"'{name.title()}' not found!")
    elif cmd =="d":
        name = input("Enter the name of the person you want to remove: ").lower()
        if name in phonebook:
            phonebook.pop(name)
        else:
            print("The person you entered was not in your phonebook!")
    elif cmd == "c":
        for name in phonebook:
            print(name,"----",phonebook[name])
    elif cmd=="q":
        break
