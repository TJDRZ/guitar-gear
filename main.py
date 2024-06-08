import uuid

ledger = []

def insert_item():
    item_name = input("Enter item name: ")
    item_cost = input("Enter item cost: ")
    ledger.append((uuid.uuid4(), item_name, item_cost))

while(True):
    print("Please choose from the following:\n",
            "1: Show full ledger\n",
            "2: Calculate total costs\n",
            "3: Add an item\n",
            "4: Update an item\n",
            "5: Delete an item\n",
            "0: Exit\n")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        for item in ledger:
            print(item[1], ": $", item[2])
        print("\n")
        
    elif choice == 2:
        print("TBD")
        print("\n")

    elif choice == 3:
        insert_item()
        print("\n")
        
    elif choice == 4:
        print("TBD")
        print("\n")

    elif choice == 5:
        print("TBD")
        print("\n")

    elif choice == 0:
        break

    else:
        print("Please choose a proper option.\n")
