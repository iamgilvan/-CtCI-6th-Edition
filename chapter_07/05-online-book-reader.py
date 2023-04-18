class User:
    def __init__(self, id, details, account_type):
        self.id = id
        self.details = details
        self.account_type = account_type

    def get_id(self):
        return self.id

    def get_details(self):
        return self.details

    def set_details(self, details):
        self.details = details

    def set_id(self, id):
        self.id = id

    def set_account_type(self, account_type):
        self.account_type = account_type

    def get_account_type(self):
        return self.account_type

    def renew_membership(self):
        pass

class UserManager:
    def __init__(self):
        self.users = {}

    def add_user(self, id, details, account_type):
        if id in self.users.keys():
            return None
        user = User(id, details, account_type)
        self.users[id] = user
        return user

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, id, details):
        if id in self.books.keys():
            return None
        book = book(id, details)
        self.books[id] = book
        return book

    def remove_book(self, id):
        if id not in self.books.keys():
            return False
        del self.books[id]

class Book:
    def __init__(self, id, details):
        self.id = id
        self.details = details

    def get_id(self):
        return self.id

    def get_details(self):
        return self.details

    def set_details(self, details):
        self.details = details

    def set_id(self, id):
        self.id = id

    def find_book(self, id):
        return self.books[id]

class Display:
    def __init__(self):
        self.active_book = None
        self.active_user = None
        self.page_number = 0

    def display_user(self, user):
        self.active_user = user
        self.refresh_username();

    def display_book(self, book):
        self.page_number = 0
        self.active_book = book

        self.refresh_title();
        self.refresh_details();
        self.refresh_page();

    def turn_page_backward(self):
        # add min page validation
        self.page_number -= 1
        self.refresh_page();

    def turn_page_forward(self):
        # add max page validation
        self.page_number += 1
        self.refresh_page();

    def refresh_username(self):
        # update username display
        pass

    def refresh_page(self):
        # update page display
        pass

    def refresh_title(self):
        # update title display
        pass

    def refresh_details(self):
        # update details display
        pass

class OnlineReaderSystem:
    def __init__(self):
        self.userManager = UserManager()
        self.library = Library()
        self.display = Display()
        self.activeBook = Book()
        self.activeUser = User()

    def get_library(self):
        return self.library

    def get_user_manager(self):
        return self.userManager

    def get_display(self):
        return self.display

    def get_active_book(self):
        return self.activeBook

    def set_active_book(self, book):
        self.activeBook = book
        self.display.display_book(book)

    def get_active_user(self):
        return self.activeUser

    def set_active_user(self, user):
        self.activeUser = user
        self.display.display_user(user)