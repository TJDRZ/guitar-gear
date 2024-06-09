import uuid

def insert_item(conn, cursor):
    try:
        item_name = input("Enter item name: ")
        item_cost = input("Enter item cost: ")

        cursor.execute("""INSERT INTO guitargear (uuid, item, cost) VALUES (
                    %s, %s, %s
                    );""",
                    (uuid.uuid4(), item_name, float(item_cost)))
    except:
        print("ERROR: Proper cost entry required.\n")

    conn.commit()
