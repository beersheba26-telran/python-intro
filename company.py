from employee import Employee
from abc import ABC, abstractmethod
from typing import Iterable
class Company(ABC):
    @abstractmethod
    def hireEmployee(empl:Employee):
        '''
        adding new Employee
        if employee with given id already exists, it throws EmployeeAlreadyExistsError
        '''
        
        pass
    @abstractmethod
    def fireEmployee(id: str):
        '''
        removing employee
        returns removed employee data
        if employee with given id doesn't exist, it throws EmployeeNofFoundError
        '''
        
        pass
    @abstractmethod
    def getAllEmployees()-> Iterable[Employee]:
        '''
        returns any iterable for iterating over all employees in  company
        if no employees exist emty iterable should be returned
        '''
        pass
    @abstractmethod    
    def getEmployeesByDepartment(department:str)-> Iterable[Employee]:
        '''
        returns an iterable for iterating over employees working in given department
        if no employees exist empty iterable should be returned
        '''
        pass
    @abstractmethod   
    def getEmployeesBySalary(fromSalary: int, toSalary: int)-> Iterable[Employee]: 
        '''
        returns an iterable for iterating over employees having salary in [fromSalary-toSalary]
        if no employees exist empty iterable should be returned
        '''
        pass
    @abstractmethod
    def getEmployeesByAge(fromAge: int, toAge: int)-> Iterable[Employee]:
        '''
        returns an iterable for iterating over employees with age in [fromAge -toAge]
        if no employees exist empty iterable should be returned
        '''
        pass
    @abstractmethod
    def getEmployee(id:str)->Employee:
        '''
        returns employee with given id
        if no employee exists it throws exception EmployeeNofFoundError
        '''
        
            
        