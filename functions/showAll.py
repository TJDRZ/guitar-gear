def show_all(conn, cursor):
    cursor.execute("SELECT * FROM guitargear;")
    
    for row in cursor.fetchall():
        print(row[1], "- $", row[2])

    conn.commit()
