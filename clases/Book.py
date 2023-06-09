from User import User

class Book:
    def __init__(self, name, ID, title, author, ISBN, yearpub):
        super().__init__(name, ID)
        self.__title = title
        self.__author = author
        self.__ISBN = ISBN
        self.__yearpub = yearpub

    def get_title(self):
        return self.__title

    def set_title(self, title):
        self.__title = title

    def get_author(self):
        return self.__author

    def set_author(self, author):
        self.__author = author

    def get_ISBN(self):
        return self.__ISBN

    def set_ISBN(self, ISBN):
        self.__ISBN = ISBN

    def get_yearpub(self):
        return self.__yearpub

    def set_yearpub(self, yearpub):
        self.__yearpub = yearpub

    def show_duedt(self):
        print("Due date: June 30, 2023")

    def reserstatus(self, option):
        if self.__title == option:
            print("You reserved that book")
        else:
            print("You cannot reserve that book")

    def requeststat(self, option):
        if self.__title == option:
            print("Book status: Available")
        else:
            print("Book status: Unavailable")

    def rewn_info(self, option):
        if self.__title == option:
            print("Renewal information: You can renew this book for 7 more days")
        else:
            print("This book cannot be renewed")

    def bookdetails(self):
        while True:
            print("1. Show Due Date")
            print("2. Check Reservation Status")
            print("3. Check Request Status")
            print("4. Get Renewal Information")
            print("5. Exit")
            choice = input("Enter your choice: ")

            if choice == "1":
                self.show_duedt()
            elif choice == "2":
                option = input("Enter the book title: ")
                self.reserstatus(option)
            elif choice == "3":
                option = input("Enter the book title: ")
                self.requeststat(option)
            elif choice == "4":
                option = input("Enter the book title: ")
                self.rewn_info(option)
            elif choice == "5":
                print("Exiting the menu...")
                break
            else:
                print("Invalid choice. Please try again.")