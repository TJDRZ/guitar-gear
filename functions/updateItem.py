def update_item(conn, cursor):
    cursor.execute("SELECT * FROM guitargear;")
    
    ledger = cursor.fetchall()

    row_number = 1

    for row in ledger:
        print(row_number, ":", row[1], "- $", row[2])
        row_number += 1

    print("\n")

    while(True):
        choice = input("Enter a row to update (0 to exit): ")

        print("\n")

        try:
            if int(choice) <= len(ledger) and int(choice) > 0:
                while(True):
                    print("Please choose from the following:\n",
                        "1: Update item name\n",
                        "2: Update item cost\n",
                        "0: Exit\n")
                    
                    column_choice = input("Enter your choice: ")

                    print("\n")

                    if column_choice == "1":
                        new_name = input("Enter new name: ")

                        cursor.execute("""UPDATE guitargear
                                    SET item = %s
                                    WHERE uuid = %s;""",
                                    (new_name, ledger[int(choice) - 1][0]))

                        return
                    
                    elif column_choice == "2":
                        new_cost = input("Enter new cost: ")

                        cursor.execute("""UPDATE guitargear
                                    SET cost = %s
                                    WHERE uuid = %s;""",
                                    (new_cost, ledger[int(choice) - 1][0]))

                        return
                    
                    elif column_choice == "0":
                        return

                    else:
                        print("Please choose a proper option.\n")

            elif choice == "0":
                return

            else:
                print("Row does not exist.\n")
            
        except:
            print("Please choose a proper option.\n")
    
    conn.commit()
