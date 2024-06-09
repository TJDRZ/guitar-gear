def combined_costs(conn, cursor):
    cursor.execute("SELECT cost FROM guitargear;")

    total = 0
        
    for row in cursor.fetchall():
        total = total + row[0]

    print(total)

    conn.commit()

