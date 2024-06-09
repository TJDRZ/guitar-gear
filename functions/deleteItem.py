def delete_item(conn, cursor):
    cursor.execute("SELECT * FROM guitargear;")
    
    ledger = cursor.fetchall()

    row_number = 1

    for row in ledger:
        print(row_number, ":", row[1], "- $", row[2])
        row_number += 1

    print("\n")

    while(True):
        choice = input("Enter a row to delete (0 to exit): ")

        print("\n")

        try:
            if int(choice) <= len(ledger) and int(choice) > 0:
                cursor.execute("DELETE FROM guitargear WHERE uuid = %s;", (ledger[int(choice) - 1][0],))
                conn.commit()
                return

            elif choice == "0":
                return

            else:
                print("Row does not exist.\n")
            
        except:
            print("Please choose a proper option.\n")
