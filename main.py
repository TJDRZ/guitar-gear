from dotenv import load_dotenv
import psycopg2
import psycopg2.extras
import os
import uuid

load_dotenv()

psycopg2.extras.register_uuid()

conn = psycopg2.connect(host = os.getenv("HOST"), dbname = os.getenv("DBNAME"), user = os.getenv("USER"), password = os.getenv("PASSWORD"), port = os.getenv("PORT"))

cursor = conn.cursor()

def insert_item():
    item_name = input("Enter item name: ")
    item_cost = input("Enter item cost: ")
    cursor.execute("""INSERT INTO guitargear (uuid, item, cost) VALUES (
                   %s, %s, %s
                   );""",
                   (uuid.uuid4(), item_name, int(item_cost)))
    conn.commit()

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
        # for item in ledger:
        #     print(item[1], ": $", item[2])
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
        cursor.close()
        conn.close()
        break

    else:
        print("Please choose a proper option.\n")
