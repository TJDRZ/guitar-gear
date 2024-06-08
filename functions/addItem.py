import uuid

def insert_item(conn, cursor):
    item_name = input("Enter item name: ")
    item_cost = input("Enter item cost: ")
    cursor.execute("""INSERT INTO guitargear (uuid, item, cost) VALUES (
                   %s, %s, %s
                   );""",
                   (uuid.uuid4(), item_name, int(item_cost)))
    conn.commit()
