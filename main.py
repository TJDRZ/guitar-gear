import uuid

ledger = []

def insert_item():
    item_name = input("Enter item name: ")
    item_cost = input("Enter item cost: ")
    ledger.append((uuid.uuid4(), item_name, item_cost))

while(len(ledger) < 3):
    insert_item()
    print(ledger)
