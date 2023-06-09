class User:
    def __init__(self,name,Id):
        self.name = name
        self.id = Id

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setId(self, ID):
        self.id = ID

    def getId(self):
        return self.id

    def verification(self):
        if self.name == "Daniela" and self.id == 12345:
            print("Verification successful")
        else:
            print("Verification failed")

    def checkAccount(self):
        if self.name == "Daniela" and self.id == 12345:
            print("This account is already created")
        else:
            print("This account is not created yet")

    def bookInfo(self):
        while True:
            print("Book info\nPlease select a book:")
            print("1. To Kill a Mockingbird")
            print("2. 1984")
            print("3. Pride and Prejudice")
            print("4. The Great Gatsby")
            print("5. The Alchemist")
            print("6. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("To Kill a Mockingbird by Harper Lee:")
                print("Author: Harper Lee")
                print("Published: 1960")
                print("Genre: Fiction, Coming-of-Age")
                print("Summary: Set in the 1930s in a small Southern town, the novel follows Scout Finch, a young girl, as she witnesses racial injustice and prejudice. Through her father, Atticus Finch, a lawyer who defends a black man accused of rape, the story explores themes of morality, compassion, and the loss of innocence.")
            elif choice == "2":
                print("1984 by George Orwell:")
                print("Author: George Orwell")
                print("Published: 1949")
                print("Genre: Dystopian Fiction")
                print("Summary: Set in a totalitarian society ruled by the Party, the novel follows Winston Smith, a low-ranking member who rebels against the oppressive regime. Orwell's dystopian vision explores themes of government surveillance, manipulation, and the power of language, creating a cautionary tale about the dangers of authoritarianism.")
            elif choice == "3":
                print("Pride and Prejudice by Jane Austen:")
                print("Author: Jane Austen")
                print("Published: 1813")
                print("Genre: Classic Literature, Romance")
                print("Summary: Set in early 19th-century England, the novel focuses on the Bennet family, particularly Elizabeth Bennet, as she navigates societal expectations, love, and personal growth. Austen's work explores themes of class, marriage, and the power of first impressions, offering sharp social commentary and memorable characters.")
            elif choice == "4":
                print("The Great Gatsby by F. Scott Fitzgerald:")
                print("Author: F. Scott Fitzgerald")
                print("Published: 1925")
                print("Genre: Literary Fiction")
                print("Summary: Set in the Jazz Age of 1920s America, the novel follows Jay Gatsby, a wealthy and enigmatic man, through the eyes of narrator Nick Carraway. Through themes of wealth, love, and the American Dream, Fitzgerald examines the disillusionment and decadence of the era, revealing the emptiness beneath the surface of the glamorous lifestyle.")
            elif choice == "5":
                print("The Alchemist by Paulo Coelho:")
                print("Author: Paulo Coelho")
                print("Published: 1988")
                print("Genre: Fiction, Inspirational")
                print("Summary: The story follows Santiago, a young shepherd, as he embarks on a journey to find his personal legend and fulfill his dreams. Through encounters with various characters, Coelho weaves a philosophical tale that explores the importance of following one's passions, listening to one's heart, and finding meaning in life's journey.")
            elif choice == "6":
                print("Exiting book info.")
                break
            else:
                print("Invalid choice. Please try again.")