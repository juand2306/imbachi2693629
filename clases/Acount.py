from User import User

class Account(User):
    def __init__(self, name, ID):
        super().__init__(name, ID)
        self.__noborbook = 0
        self.__noresbook = 0
        self.__nortubook = 0
        self.__nolostbook = 0
        self.__fineamount = 0
    
    def display_menu(self):
        print("------ Library Menu ------")
        print("1. Borrow a book")
        print("2. Reserve a book")
        print("3. Return a book")
        print("4. Mark a book as lost")
        print("5. Check fine amount")
        print("6. Exit")
    
    def borrow_book(self):
        book = input("Enter the book you want to borrow: ")
        print("Borrowing book:", book)
        # Update the necessary book counts and perform other operations
        
    def reserve_book(self):
        book = input("Enter the book you want to reserve: ")
        print("Reserving book:", book)
        # Update the necessary book counts and perform other operations
        
    def return_book(self):
        book = input("Enter the book you want to return: ")
        print("Returning book:", book)
        # Update the necessary book counts and perform other operations
        
    def mark_lost_book(self):
        book = input("Enter the book you want to mark as lost: ")
        print("Marking book as lost:", book)
        # Update the necessary book counts and perform other operations
        
    def check_fine_amount(self):
        book = input("Enter the book to check fine amount: ")
        print("Checking fine amount for book:", book)
        # Calculate the fine amount and display it
    
    def run_menu(self):
        while True:
            self.display_menu()
            choice = input("Enter your choice: ")
            
            if choice == "1":
                self.borrow_book()
            elif choice == "2":
                self.reserve_book()
            elif choice == "3":
                self.return_book()
            elif choice == "4":
                self.mark_lost_book()
            elif choice == "5":
                self.check_fine_amount()
            elif choice == "6":
                print("Exiting menu.")
                break
            else:
                print("Invalid choice. Please try again.")