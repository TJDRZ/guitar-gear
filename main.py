from db.connectDB import connectDB
from functions import showAll, combinedCosts, addItem

db = connectDB()

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
        showAll.show_all(db["conn"], db["cursor"])
        print("\n")
        
    elif choice == 2:
        combinedCosts.combined_costs(db["conn"], db["cursor"])
        print("\n")

    elif choice == 3:
        addItem.insert_item(db["conn"], db["cursor"])
        print("\n")
        
    elif choice == 4:
        print("TBD")
        print("\n")

    elif choice == 5:
        print("TBD")
        print("\n")

    elif choice == 0:
        db["cursor"].close()
        db["conn"].close()
        break

    else:
        print("Please choose a proper option.\n")
