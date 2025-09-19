class  library :
    def __init__(self):
        self.book = []
    
    def add_book(self):
            title = input("Enter the title of the book: ")
            subject = input("Enter the subject of the book: ")
            self.book.append({"title": title, "subject": subject})
            print(f"Book '{title}' added successfully.")   


    def remove_book(self):
            title = input("Enter the title of the book you want to remove: ")
            for book in self.book:
                if book["title"] == title:
                    self.book.remove(book)
                    print(f"Book '{title}' removed successfully.")
                    return
            print(f"Book '{title}' not found.")

    def update_book(self):
            title = input("Enter the title of the book you want to update: ")
            for book in self.book:
                if book["title"] == title:
                    new_title = input("Enter the new title of the book: ")
                    new_subject = input("Enter the new subject of the book: ")
                    book["title"] = new_title
                    book["subject"] = new_subject
                    print(f"Book '{title}' updated successfully.")
                    return
            print(f"Book '{title}' not found.")


    def show_books(self):
            if self.book:
                print("List of available books:")
                for book in self.book:
                    print("--------------------------")
                    print("Title:", book["title"])
                    print("Subject:", book["subject"])
                    print("--------------------------")
            else:
                print("No books available in the library.")

library = library()

while True:
    print("\nMenu:")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Update a book")
    print("4. Show available books")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.remove_book()
    elif choice == "3":
        library.update_book()
    elif choice == "4":
        library.show_books()
    elif choice == "5":
        print("Exiting the program.")
        break
    else:
        print("Invalid choice! Please choose a number between 1 and 5.")