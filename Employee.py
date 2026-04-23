import json
class Employee:
    id: str
    name: str
    birthdate: str
    department: str
    salary: int
    def __init__(self,*,id:str,name:str,birthdate:str,department:str, salary:int):
        self.id = id
        self.birthdate = birthdate
        self.department = department
        self.name = name
        self.salary = salary
    def __eq__(self, other)->bool:
        return self.id == other.id if isinstance(other, Employee) else NotImplemented
    def __lt__(self, other)->bool:
        return self.id < other.id if isinstance(other, Employee) else NotImplemented
    def __str__(self)->str:
        return json.dumps(self.__dict__)
        
            

   