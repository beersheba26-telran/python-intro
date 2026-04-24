class EmployeeAlreadyExists(Exception):
    def __init__(self, id: str):
        super().__init__(f"employee with id {id} already exists")
        
class EmployeeNotFoundError(Exception):
    def __init__(self, id: str) :
        super().__init__(f"employee with id {id} doesn't exist" )     