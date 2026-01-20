# Library Management System - Final Project
# Concepts: Classes, Dicts, Sets, List Comprehensions, and Functions

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Member:
    def __init__(self, name):
        self.member_name = name

# --- Data Structures ---
books = {}        # Dict: {book_id: BookObject}
members = {}      # Dict: {member_id: MemberObject}
issued_books = set()  # Set: Stores book_ids that are currently out
transactions = [] # List of dicts: To log every borrow/return

def main():
    while True:
        print("\n=== LIBRARY SYSTEM MENU ===")
        print("1. Add Book/Member (Create)")
        print("2. Update Book/Member (Update)")
        print("3. Remove Book/Member (Delete)")
        print("4. Search & Filter Books (Read)")
        print("5. Borrow Book")
        print("6. Return Book")
        print("7. View Transaction History")
        print("8. Exit")
        
        choice = input("\nSelect an option: ")

        # --- 1. ADD RECORDS (CRUD: Create) ---
        if choice == "1":
            sub_type = input("Add (B)ook or (M)ember? ").upper()
            if sub_type == "B":
                bid = input("Enter Book ID: ")
                t = input("Enter Title: ")
                a = input("Enter Author: ")
                books[bid] = Book(t, a)
                print("Book recorded.")
            elif sub_type == "M":
                mid = input("Enter Member ID: ")
                n = input("Enter Name: ")
                members[mid] = Member(n)
                print("Member recorded.")

        # --- 2. UPDATE RECORDS (CRUD: Update) ---
        elif choice == "2":
            up_type = input("Update (B)ook or (M)ember? ").upper()
            if up_type == "B":
                bid = input("Enter Book ID to update: ")
                if bid in books:
                    books[bid].title = input("New Title: ")
                    books[bid].author = input("New Author: ")
                    print("Book updated.")
                else:
                    print("ID not found.")

        # --- 3. REMOVE RECORDS (CRUD: Delete) ---
        elif choice == "3":
            del_id = input("Enter ID to remove: ")
            if del_id in books:
                del books[del_id]
                print("Book deleted.")
            elif del_id in members:
                del members[del_id]
                print("Member deleted.")
            else:
                print("ID does not exist.")

        # --- 4. SEARCH & FILTER ---
        elif choice == "4":
            keyword = input("Enter title keyword to filter: ").lower()
            # List Comprehension used here to show off the concept
            results = [b.title for b in books.values() if keyword in b.title.lower()]
            
            print("Matching Books:", results if results else "No matches.")

        # --- 5. BORROW (Transaction + Set usage) ---
        elif choice == "5":
            bid = input("Enter Book ID to borrow: ")
            mid = input("Enter Member ID: ")
            
            # Logic check using membership operators
            if bid in books and mid in members:
                if bid not in issued_books:
                    issued_books.add(bid) # Adding to Set
                    # Log transaction as a dictionary
                    log = {"action": "Borrow", "book": books[bid].title, "member": members[mid].member_name}
                    transactions.append(log)
                    print("Book issued successfully.")
                else:
                    print("Error: Book is already issued.")
            else:
                print("Error: Invalid IDs.")

        # --- 6. RETURN ---
        elif choice == "6":
            bid = input("Enter Book ID to return: ")
            if bid in issued_books:
                issued_books.remove(bid) # Remove from Set
                log = {"action": "Return", "book": books[bid].title}
                transactions.append(log)
                print("Book returned.")
            else:
                print("This book was not issued.")

        # --- 7. TRANSACTION HISTORY ---
        elif choice == "7":
            print("\n--- Transaction Log ---")
            for entry in transactions:
                # Accessing dictionary keys
                if entry["action"] == "Borrow":
                    print(entry["member"] + " borrowed " + entry["book"])
                else:
                    print("Book '" + entry["book"] + "' was returned.")

        elif choice == "8":
            break

if __name__ == "__main__":
    main()
