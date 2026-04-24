from datetime import date

from company import Company
from employee import Employee
from company_exceptions import EmployeeAlreadyExists, EmployeeNotFoundError
from typing import Callable
class __CompanyImpl(Company):
    employees: dict[str, Employee] = dict() # key - id, value - Employee
    employeesDepartment: dict[str, list[Employee]] = dict() # key - department, value - list of employees in department
    
    def hireEmployee(self, empl):
        if empl.id in self.employees: 
            raise EmployeeAlreadyExists(empl.id)
        self.employees[empl.id] = empl
        self.employeesDepartment.setdefault(empl.department, []).append(empl)
    def fireEmployee(self, id):
        if id not in self.employees:
            raise EmployeeNotFoundError(id)
        emplRes = self.employees.pop(id)
        self.__remove_employee_from_dep_index(emplRes)
        return emplRes

    def __remove_employee_from_dep_index(self, emplRes):
        employeesInDepartment = self.employeesDepartment.get(emplRes.department)
        employeesInDepartment.remove(emplRes)
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
    def __getEmployeesByPredicate(self, pred: Callable[[Employee], bool]):
        return (empl for empl in self.employees.values() if pred(empl))
    def getEmployeesByAge(self, fromAge, toAge):
        dateMin = _getDateFromAge(toAge, 1, 1)
        dateMax = _getDateFromAge(fromAge, 12, 31)
        return self.__getEmployeesByPredicate(lambda empl:  dateMin <= empl.birthdate <= dateMax)
    def getEmployeesBySalary(self, fromSalary, toSalary):
        return self.__getEmployeesByPredicate(lambda empl: fromSalary <= empl.salary <= toSalary)
def _getDateFromAge(age:int, month, day)->str:
    today = date.today()
    return date(today.year - age, month, day).isoformat()
    
companyInstance: Company = __CompanyImpl()            