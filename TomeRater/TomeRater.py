class User(object):
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.books = {}

    def get_email(self):
        return self.email

    def change_email(self, address):
        self.email = address
        print("This User's email has been updated.")

    def __repr__(self):
        info = "User: " + self.name + ", email: " + self.email + ", books read: " + str(len(self.books))
        return info

    def __eq__(self, other_user):
        if self.name == other_user.name and self.email == other_user.email:
            return "Users are equal"

    def read_book(self, book, rating=None):
        self.books[book] = rating

    def get_average_rating(self):
        total = 0
        avg = 0
        count = 0

        for i in self.books.keys():
            if self.books[i] != None:
                total += self.books[i]
                count += 1
            else:
                pass
        avg = total/count
        return avg

class Book():
    def __init__(self, title, isbn):
        self.title = title
        self.isbn = isbn
        self.ratings = []

    def get_title(self):
        return self.title

    def get_isbn(self):
        return self.isbn

    def set_isbn(self, isbn):
        self.isbn = isbn
        print("This book's ISBN has been updated.")

    def add_rating(self, rating):
        if rating:
            if rating <= 4 and rating >= 0:
                self.ratings.append(rating)
            else:
                print("Invalid Rating")

    def __eq__(self, other_book):
        if self.title == other_book.title and self.isbn == other_book.isbn:
            return "Books are equal"

    def get_average_rating(self):
        total = 0
        avg = 0

        for i in self.ratings:
            total += i
        avg = total / len(self.ratings)
        return avg

    def __hash__(self):
        return hash((self.title, self.isbn))

class Fiction(Book):
    def __init__(self, title, author, isbn):
        super().__init__(title, isbn)
        self.author = author

    def get_author(self):
        return self.author

    def __repr__(self):
        phrase = self.title + " by " + self.author
        return phrase

class Non_Fiction(Book):
    def __init__(self, title, subject, level, isbn):
        super().__init__(title, isbn)
        self.subject = subject
        self.level = level

    def get_subject(self):
        return self.subject

    def get_level(self):
        return self.level

    def __repr__(self):
        phrase = self.title + ", a " + self.level + " manual on " + self.subject
        return phrase

class TomeRater():
    def __init__(self):
        self.users = {}
        self.books = {}

    def create_book(self, title, isbn):
        return Book(title, isbn)

    def create_novel(self, title, author, isbn):
        return Fiction(title, author, isbn)

    def create_non_fiction(self, title, subject, level, isbn):
        return Non_Fiction(title, subject, level, isbn)

    def add_book_to_user(self, book, email, rating=None):
        if email not in self.users:
            print("No user with email " + self.email)
        else:
            self.users[email].read_book(book, rating)
            if book in self.books:
                self.books[book] += 1
            else:
                self.books[book] = 0
            book.add_rating(rating)

    def add_user(self, name, email, user_books=None):
        user2 = User(name, email)
        self.users[email] = user2

        if user_books != None:
            for book in user_books:
                self.add_book_to_user(book, email)

    def print_catalog(self):
        for book in self.books.keys():
            print(book)

    def print_users(self):
        for user in self.users.values():
            print(user)

    def most_read_book(self):
        return max(self.books, key=self.books.get)

    def highest_rated_book(self):
        book_rating = 0
        book_rated = None

        for i in self.books:
            book_avg = i.get_average_rating()
            if book_avg > book_rating:
                book_rating = book_avg
                book_rated = book
            return book_rated

    def most_positive_user(self):
        high_rating = 0
        pos_user = None
        for i in self.users.values():
            user_avg = i.get_average_rating()
            if user_avg > high_rating:
                high_rating = user_avg
                pos_user = i
        return pos_user

    def get_n_most_prolific_readers(self, n):