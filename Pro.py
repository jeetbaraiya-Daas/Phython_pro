books_db = {}      # Dictionary for book data
members_db = {}    # Dictionary for member data
out_set = set()    # Set for book IDs
history = []       # List for trans logs

# add a new book
def add_new_book():
    bid = input("Enter ID: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    cat = input("Enter Category: ")
    
    details = (author, cat)
    
    books_db[bid] = {
        'title': title,
        'info': details
    }
    print("Added to system.")

# Recursion Search Function
def find_book_recursive(data_list, target, idx=0, matches=None):
    if matches is None:
        matches = []
        
    # Base Case
    if idx == len(data_list):
        return matches
    
    if target in data_list[idx]['title'].lower():
        matches.append(data_list[idx]['title'])
    
    return find_book_recursive(data_list, target, idx + 1, matches)

# Bubble Sort 
def show_books_sorted():
    if not books_db:
        print("Empty library.")
        return
     
    # dict to liat
    b_list = list(books_db.values())
    n = len(b_list)

    # --- Bubble Sort Logic ---
    for i in range(n):
        for j in range(0, n - i - 1):
            # Compare titles (A-Z)
            if b_list[j]['title'] > b_list[j + 1]['title']:
                # Swap the elements
                temp = b_list[j]
                b_list[j] = b_list[j + 1]
                b_list[j + 1] = temp

    print("\n--- Books (A to Z) ---")
    for b in b_list:
        print(f"Title: {b['title']} | Author: {b['info'][0]}")

# Borrow logic
def issue_process():
    bid = input("Book ID: ")
    mid = input("Member ID: ")
    
    if bid in books_db and mid in members_db:
        if bid not in out_set:
            out_set.add(bid)
            
            # Use .insert() to add in list 
            log_entry = {"msg": f"{members_db[mid]['name']} took {books_db[bid]['title']}"}
            history.insert(0, log_entry) 
            
            print("Issue successful.")
        else:
            print("Book is not available.")
    else:
        print("Invalid ID.")

def main():
    while True:
        print("\n--- MENU ---")
        print("1. Add Book")
        print("2. Add Member")
        print("3. Search (Recursion)")
        print("4. View All (Bubble Sort)")
        print("5. Borrow Book")
        print("6. Show History")
        print("7. Exit")
        
        choice = input("Select: ")
        
        match choice:
            case "1":
                add_new_book()
                
            case "2":
                mid = input("Member ID: ")
                name = input("Name: ")
                members_db[mid] = {'name': name}
                print("Member added.")
                
            case "3":
                word = input("Search for: ").lower()
                all_books = list(books_db.values())
                found = find_book_recursive(all_books, word)
                print("Matches found:", found)
                
            case "4":
                show_books_sorted()
                
            case "5":
                issue_process()
                
            case "6":
                print("\n--- Recent Activity ---")
                for item in history:
                    print(item['msg'])
                    
            case "7":
                print("Closing...")
                break
                
            case _:
                print("Try again.")

 main()
