import os
import sqlite3
from tabulate import tabulate

# connection to the db
con = sqlite3.connect(".//contact.db")

cur = con.cursor()

class Contact():
    
    def display(self):
        # query result
        res = cur.execute(
            """SELECT COUNT(*) 
            FROM contacts"""
            ).fetchall()

        # display query result
        if res[0][0]==0:
            print("You have no saved contacts.")
        else:
            data = [
                [contact_id, name, number] \
                    for contact_id, name, number in cur.execute(
                """SELECT id, name, number
                FROM contacts 
                ORDER BY name 
                ASC"""
                )
                ]
            print(tabulate(
                data, 
                headers=["S/N", "Name", "Number"], 
                tablefmt="outline"
                ))
        print()

    def add_contact(self):
        # get contact details
        name = input("Contact Name: ")
        number = input("Phone Number: ")
        email = input("Email: ")
        address = input("Address: ")

        # add contact detail to database
        detail = (name, number, email, address)

        if name and number and email and address:
            cur.execute(
                """INSERT INTO contacts 
                (name, number, email, address) 
                VALUES(?, ?, ?, ?)""", 
                detail
                )
            con.commit()
        
        os.system('cls||clear')

    def contact_detail(self):
        # get and verify contact S/N
        try:
            no = int(input("Contact S/N: "))
        except ValueError:
            print("S/N must be a number")
        else:
            nos = [contact_id[0] for contact_id in cur.execute(
                    """SELECT id
                    FROM contacts"""
                    )]
            
            # verify contact no, query database and display details
            if no in nos:
                data = [
                    [contact_id, name, number, email, address] \
                        for contact_id, name, number, email, address \
                            in cur.execute(
                    """SELECT *
                    FROM contacts
                    WHERE id = ?""",
                    str(no)
                    )]
                
                os.system('cls||clear')

                print(tabulate(
                    data, 
                    headers=["S/N", "Name", "Number", "E-Mail", "Address"], 
                    tablefmt="outline"
                    ))
            else:
                print("Contact does not exist!")
            print()

    def search(self):
        print()
        print("Type: n - search using name, p - search using number")
        print()

        command = input(">> ")
        if command == "n":
            name = input("Contact Name: ")
            name = f"%{name}%"

            res = cur.execute(
                """SELECT COUNT(*) 
                FROM contacts
                WHERE name LIKE ?
                COLLATE NOCASE""",
                (name,)
                ).fetchall()

            if res[0][0]==0:
                print("Contact does not exist!")
            else:

                data = [
                    [contact_id, name, number, email, address] \
                        for contact_id, name, number, email, address \
                            in cur.execute(
                        """SELECT *
                        FROM contacts
                        WHERE name LIKE ?
                        COLLATE NOCASE""",
                        (name,)
                        )]
                print(tabulate(
                    data, 
                    headers=["S/N", "Name", "Number", "E-Mail", "Address"],
                    tablefmt="outline"
                    ))
                print()

        elif command == "p":
            number = input("Contact Number: ")
            number = f"%{number}%"

            res = cur.execute(
                """SELECT COUNT(*) 
                FROM contacts
                WHERE number LIKE ?
                COLLATE NOCASE""",
                (number,)
                ).fetchall()

            if res[0][0]==0:
                print("Contact does not exist!")
            else:
                data = [
                    [contact_id, name, number, email, address] \
                        for contact_id, name, number, email, address \
                            in cur.execute(
                        """SELECT *
                        FROM contacts
                        WHERE number LIKE ?
                        COLLATE NOCASE""",
                        (number,)
                        )]
                
                os.system('cls||clear')

                print(tabulate(
                    data, 
                    headers=["S/N", "Name", "Number", "E-Mail", "Address"], 
                    tablefmt="outline"
                    ))
                print()
        else:
            print("Invalid command!")

    def update_contact(self):
        try:
            no = int(input("Contact S/N: "))
        except ValueError:
            print("S/N must be a number")
        else:
            nos = [contact_id[0] for contact_id in cur.execute(
                    """SELECT id
                    FROM contacts"""
                    )]
            
            if no in nos:
                print(
"""Type: n - Change Name, p - Change number, 
      e - Change email, a - Change address"""
                    )
                command = input(">> ")

                if command not in ["n", "p", "e", "a"] or not command:
                    print("Invalid Command!")
                    print()
                elif command == "n":
                    new_name = input("New Contact Name: ")
                    if new_name:
                        detail = (new_name, no)

                        cur.execute(
                        """UPDATE contacts
                            SET name = ?
                            WHERE id = ?""",
                            detail
                            )
                        con.commit()

                        os.system('cls||clear')

                        print("Updated Successfully!") 
                elif command == "p":
                    new_number = input("New Contact Number: ")
                    if new_number:
                        detail = (new_number, no)

                        cur.execute(
                        """UPDATE contacts
                            SET number = ?
                            WHERE id = ?""",
                            detail
                            )
                        con.commit()

                        os.system('cls||clear')

                        print("Updated Successfully!") 
                elif command == "e":
                    new_email = input("New Contact E-mail: ")
                    if new_number:
                        detail = (new_email, no)

                        cur.execute(
                        """UPDATE contacts
                            SET email = ?
                            WHERE id = ?""",
                            detail
                            )    
                        con.commit()

                        os.system('cls||clear')

                        print("Updated Successfully!") 
                elif command == "a":
                    new_address = input("New Contact Address: ")
                    if new_address:
                        detail = (new_address, no)

                        cur.execute(
                        """UPDATE contacts
                            SET address = ?
                            WHERE id = ?""",
                            detail
                            )
                        con.commit()

                        os.system('cls||clear')

                        print("Updated Successfully!")  
                            
                print()

    def delete_contact(self):
        try:
            no = int(input("Contact S/N: "))
        except ValueError:
            print("S/N must be a number")
        else:
            nos = [contact_id[0] for contact_id in cur.execute(
                    """SELECT id
                    FROM contacts"""
                    )]
            
            if no in nos:
                print("Are you sure you want to delete this contact?")
                print("y - yes, n - no")

                command = input(">> ")
                if command == "y":
                    cur.execute(
                        """DELETE FROM contacts
                        WHERE id = ?""",
                        (no,)
                    )
                    con.commit()
                    print("Contact deleted!")

        os.system('cls||clear')


def main():
    print("Contact Book")
    print("-------------")
    print()

    ct = Contact()

    while True:
        print(
"""Type: a - Add contact, l - View contact list,
      v - View contact detail, s - Search contacts, 
      u - Update contact, d - Delete contact
      x - Exit"""
               )
        print()

        command = input(">> ")

        if command == "a":
            ct.add_contact()
        elif command == "l":
            ct.display()
        elif command == "v":
            ct.contact_detail()
        elif command == "s":
            ct.search()
        elif command == "u":
            ct.update_contact()
        elif command == "d":
            ct.delete_contact()
        elif command == "x":
            break
        else:
            print("Invalid command!")

        print()


main()