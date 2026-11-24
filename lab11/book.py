import uuid

class Book:

    # default constructor
    def __init__(self):
        self.title = ""
        self.author = ""
        self.genre = ""
        self.book_id = str(uuid.uuid4())
        self.__state = "NOT IN INVENTORY"
        self.__borrower = ""

    # parameterized constructor
    def __init__(self, title, author, genre, state="Checked In"):
        self.title = title
        self.author = author
        self.genre = genre
        self.book_id = str(uuid.uuid4())
        self.__state = state
        self.__borrower = ""
        
    def check_in(self):
        self.__state = "CHECKED IN"
        self.__borrower = ""

    def check_out(self, borrower):
        self.__state = "CHECKED OUT"
        self.__borrower = borrower

    def get_state(self):
        return self.__state
    