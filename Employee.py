from dataclasses import dataclass, field
@dataclass(order=True, frozen=True, slots=True)
class Employee:
    id: str
    name: str = field(compare=False)
    birthdate: str = field(compare=False)
    department: str = field(compare=False)
    salary: int = field(compare=False)
   
   
   