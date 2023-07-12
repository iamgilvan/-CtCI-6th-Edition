from abc import ABC, abstractmethod
from enum import IntEnum


class User:
    def __init__(self, id, account_name, full_name):
        self.id = id
        self.account_name = account_name
        self.full_name = full_name
        self.status = None
        self.private_chat = {}
        self.group_chat = []
        self.received_add_request = {}
        self.sent_add_request = {}
        self.contacts = {}
    
    def send_message_to_user(self, to_user, message):
        pass
    
    def send_message_to_group_chat(self, id_group, message):
        pass
    
    def set_status_message(self, status):
        self.status = status
    
    def get_status_message(self):
        return self.status
    
    def add_contact(self, user):
        pass

    def get_id(self):
        return self.id
    
    def get_account_name(self):
        return self.account_name
    
    def sent_add_request(self, request):
        pass
    
    def received_add_request(self, request):
        pass
    
    def remove_add_request(self, request):
        pass
    
    def request_add_user(self, account_name):
        pass
    
    def add_conversation_private_chat(self, conversation):
        pass
    
    def add_conversation__group_chat(self, conversation):
        pass
    
class RequestStatus(IntEnum):
    Unread = 0
    Read = 1
    Accepted = 2
    Rejected = 3

class UserStatusType(IntEnum):
    Offline = 0
    Away = 1
    Idle = 2
    Available = 3
    Busy = 4

class UserStatus:
    def __init__(self, type, message):
        self.type = type
        self.message = message
        
    def get_status_type(self):
        return self.type
    
    def get_message(self):
        return self.message

class AddRequest:
    def __init__(self, from_user, to, date):
        self.from_user = from_user
        self.to = to
        self.date = date
        self.status = None
    
    def get_status(self):
        pass
    
    def get_date(self):
        pass
    
    def get_from_user(self):
        pass
    
    def get_to_user(self):
        pass

class Message:
    def __init__(self, content, date):
        self.content = content
        self.date = date
    
    def get_content(self):
        pass
    
    def get_date(self):
        pass

class Conversation(ABC):
    @property
    @abstractmethod
    def my_abstract_property(self):
        self.participants = []
        self.id = None
        self.messages = []
    @abstractmethod
    def add_message(self, message):
        pass
    
    @abstractmethod
    def get_message(self):
        pass
    
    @abstractmethod
    def get_id(self):
        pass

class GroupChat(Conversation):
    def remove_participant(user):
        pass
    
    def add_participant(user):
        pass

class PrivateChat(Conversation):
    def private_chat(user1, user2):
        pass
    
    def get_other_participant(primary_user):
        pass
    
class UserManager:
    def __init__(self):
        self.users_by_id = {}
        self.users_by_account_name = {}
        self.online_user = {}
    
    def add_user(self, from_user, to_account_name):
        pass
    
    def approved_add_request(request):
        pass
    
    def rejected_add_request(request):
        pass
    
    def user_signedon(account_name):
        pass
    
    def user_signedoff(account_name):
        pass
    