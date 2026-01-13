#

# --- Task 1: Class Definitions ---
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class Member:
    def __init__(self, name):
        self.member_name = name

# --- Global Data Storage ---
books_list = []
members_list = []
total_books = 0  # Using an integer for arithmetic practice

def start_program():
    global total_books
    
    # We use a variable to keep the loop running
    keep_running = True
    
    while keep_running:
        print("\n==============================")
        print("   LIBRARY MANAGEMENT SYSTEM   ")
        print("==============================")
        print("1. Add New Book")
        print("2. Search for a Book")
        print("3. Remove a Book")
        print("4. Add New Member")
        print("5. Remove Member")
        print("6. Show Library Stats")
        print("7. Exit")
        
        choice = input("\nEnter choice (1-7): ")

        # Task 2: Menu navigation using if-else
        if choice == "1":
            t = input("Enter Book Title: ")
            a = input("Enter Author Name: ")
            new_book = Book(t, a)
            books_list.append(new_book)
            # Arithmetic operator practice
            total_books = total_books + 1 
            print("Success: Book added to system.")

        elif choice == "2":
            query = input("Enter book title to search: ")
            
            # Create a simple list of titles for the membership operator
            titles_only = []
            for b in books_list:
                titles_only.append(b.title)
            
            # Use membership operator 'in'
            if query in titles_only:
                print("Result: Yes, we have '" + query + "' in stock.")
            else:
                print("Result: Book not found.")

        elif choice == "3":
            rem_title = input("Enter title to remove: ")
            found_book = False
            for b in books_list:
                if b.title == rem_title:
                    books_list.remove(b)
                    total_books = total_books - 1
                    found_book = True
                    print("Success: Book removed.")
                    break
            
            if not found_book:
                print("Error: Could not find that book.")

        elif choice == "4":
            m_name = input("Enter member name: ")
            new_member = Member(m_name)
            members_list.append(new_member)
            print("Success: Member registered.")

        elif choice == "5":
            rem_name = input("Enter member name to remove: ")
            found_mem = False
            for m in members_list:
                if m.member_name == rem_name:
                    members_list.remove(m)
                    found_mem = True
                    print("Success: Member removed.")
                    break
            
            if found_mem == False: # Comparison operator practice
                print("Error: Member name does not exist.")

        elif choice == "6":
            print("\n--- Current Statistics ---")
            print("Total Books: " + str(total_books)) # Type conversion
            print("Total Members: " + str(len(members_list)))
            
            # Logical and Identity operator practice
            if total_books == 0 and len(members_list) == 0:
                print("Library Status: Empty")
            else:
                print("Library Status: Active")

        elif choice == "7":
            print("Exiting... Thank you for using the system!")
            keep_running = False
            
        else:
            print("Invalid input. Please type a number from 1 to 7.")

# This starts the program
if __name__ == "__main__":
    start_program()
