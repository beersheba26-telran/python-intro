from datetime import date

from sortedcontainers import SortedKeyList, SortedSet

from company import Company
from employee import Employee
from company_exceptions import EmployeeAlreadyExists, EmployeeNotFoundError
class __CompanyImpl(Company):
    employees: dict[str, Employee] # key - id, value - Employee
    employeesDepartment: dict[str, set[Employee]] # key - department, value - list of employees in department
    employeesAge: SortedKeyList[Employee]
    employeesSalary: SortedKeyList[Employee]
    def __init__(self):
        self.employees = dict()
        self.employeesDepartment = dict()
        self.employeesAge = SortedKeyList(key = lambda e: (e.birthdate, e.id))
        self.employeesSalary = SortedKeyList(key = lambda e: (e.salary, e.id))
    def hireEmployee(self, empl):
        if empl.id in self.employees: 
            raise EmployeeAlreadyExists(empl.id)
        self.employees[empl.id] = empl
        self.employeesDepartment.setdefault(empl.department, set()).add(empl)
        self.employeesAge.add(empl)
        self.employeesSalary.add(empl)
    def fireEmployee(self, id):
        if id not in self.employees:
            raise EmployeeNotFoundError(id)
        emplRes = self.employees.pop(id)
        self.__remove_employee_from_dep_index(emplRes)
        self.employeesSalary.remove(emplRes)
        self.employeesAge.remove(emplRes)
        return emplRes

    def __remove_employee_from_dep_index(self, emplRes):
        employeesInDepartment = self.employeesDepartment.get(emplRes.department)
        employeesInDepartment.discard(emplRes)
        if not len(employeesInDepartment):
            self.employeesDepartment.pop(emplRes.department)
    def getAllEmployees(self):
        return (empl for empl in self.employees.values())
    def getEmployee(self, id):
        if id not in self.employees:
            raise EmployeeNotFoundError(id)
        return self.employees[id]
    def getEmployeesByDepartment(self, department):
        return (empl for empl in self.employeesDepartment.get(department, []))
   
    def getEmployeesByAge(self, fromAge, toAge):
        dateMin = _getDateFromAge(toAge, 1, 1)
        dateMax = _getDateFromAge(fromAge, 12, 31)
        left: int = self.employeesAge.bisect_key_left((dateMin,""))
        right: int = self.employeesAge.bisect_key_left((dateMax+"0", ""))
        return self.employeesAge[left:right]
    def getEmployeesBySalary(self, fromSalary, toSalary):
        left: int = self.employeesSalary.bisect_key_left((fromSalary,""))
        right: int = self.employeesSalary.bisect_key_left((toSalary+1, ""))
        return self.employeesSalary[left:right]
def _getDateFromAge(age:int, month, day)->str:
    today = date.today()
    return date(today.year - age, month, day).isoformat()
    
companyInstance: Company = __CompanyImpl()            