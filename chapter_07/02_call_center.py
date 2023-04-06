from enum import IntEnum
import unittest


class Rank(IntEnum):
    RESPONDENT = 0
    DIRECTOR = 1
    MANAGER = 2
    
class Employee:
    def __init__(self, call_handler):
        self.call_handler = call_handler
        self.current_call = None
        self.rank = None
    
    #Start the conversation
    def receive_call(self, call):
        self.current_call = call
    
    
    def call_completed(self):
        if self.current_call:
            self.current_call.disconnect(self)
            #self.current_call = None
        #self.assign_call()
    
    def assign_call(self):
        if not self.is_free():
            return False
        return self.call_handler.assign_call(self)
    
    def is_free(self):
        return self.current_call is None
    
    def escalate_call(self):
        if self.current_call:
            self.current_call.increment_rank()
            self.current_call.dispatch_call(self.current_call)
            #self.current_call = None
            self.current_call.disconnect(self)
        #self.assign_call()

    def get_rank(self):
        return self.rank
    
    
class Respondent(Employee):
    def __init__(self, call_handler):
        super().__init__(call_handler)
        self.rank = Rank.RESPONDENT


class Manager(Employee):
    def __init__(self, call_handler):
        super().__init__(call_handler)
        self.rank = Rank.MANAGER


class Director(Employee):
    def __init__(self, call_handler):
        super().__init__(call_handler)
        self.rank = Rank.DIRECTOR


class Caller:
    def __init__(self, id):
        self.id = id
        
class Call:
    def __init__(self, caller):
        self.caller = caller
        self.rank = Rank.RESPONDENT
        self.handler = None
    
    def set_handler(self, employee):
        self.handler = employee
    
    def set_rank(self, rank):
        self.rank = rank
    
    def get_rank(self):
        return self.rank
    
    def disconnect(self, employee):
        employee.current_call = None
        
    def increment_rank(self):
        if self.rank == Rank.RESPONDENT:
            self.rank = Rank.MANAGER
        elif self.rank == Rank.MANAGER:
            self.rank = Rank.DIRECTOR
        return self.rank

class CallHandler:
    NUM_RESPONDENT = 3
    NUM_MANAGER = 2
    NUM_DIRECTOR = 1
    LEVEL = 3
    
    def __init__(self):
        self.call_queue = [[],[],[]]
        self.employee_levels = list()
        self.employee_levels.append([Respondent(self) for _ in range(self.NUM_RESPONDENT)])
        self.employee_levels.append([Manager(self) for _ in range(self.NUM_MANAGER)])
        self.employee_levels.append([Director(self) for _ in range(self.NUM_DIRECTOR)])
        
    def get_handler_for_call(self, call):
        # we can change this to a Queue()
        for level in range(call.get_rank(), self.LEVEL):
            for employee in self.employee_levels[level]:
                if employee.is_free():
                    return employee
        return None
    
    def dispatch_call(self, caller):
        call = Call(caller)
        employee = self.get_handler_for_call(call)
        if employee:
            employee.receive_call(call)
            call.set_handler(employee)
        else:            
            self.call_queue[call.get_rank()].append(call)
            raise Exception("Every lines is full. Please wait for them.")
        
    def assign_call(self, employee):
        for rank in range(employee.get_rank(), 0, -1):
            queue = self.call_queue[rank]
            if queue:
                call = queue.pop(0)
                if call:
                    employee.receive_call(call)
                    return True
        return False
    

class Test(unittest.TestCase):
    def test_full_line(self):
        self.caller1 = Caller(1)
        self.caller2 = Caller(2)
        self.caller3 = Caller(3)
        self.caller4 = Caller(4)
        self.caller5 = Caller(5)
        self.caller6 = Caller(6)
        self.caller7 = Caller(7)
        self.call_handler = CallHandler()
        
        for _ in range(6):
            self.call_handler.dispatch_call(self.caller1)
        self.assertRaises(Exception, self.call_handler.dispatch_call, self.caller1)

if __name__ == "__main__":
    unittest.main()