from unittest import TestCase
from employee import Employee
from company_impl import companyInstance
from company_exceptions import EmployeeAlreadyExists, EmployeeNotFoundError
_empl1: Employee = Employee(birthdate="1970-10-10",id="1",name="name1",department="dep1", salary=10000)
_empl2: Employee = Employee(birthdate="1980-10-10",id="2",name="name2",department="dep1", salary=15000)
_empl3: Employee = Employee(birthdate="1990-10-10",id="3",name="name3",department="dep2", salary=20000)
_empl4: Employee = Employee(birthdate="2000-10-10",id="4",name="name4",department="dep2", salary=25000)
_empl5: Employee = Employee(birthdate="2001-10-10",id="5",name="name5",department="dep2", salary =20000)
_empl6: Employee = Employee(birthdate="2002-10-10",id="6",name="name6",department="dep3", salary=10000)
_emplForAdd = Employee(id="100",name="name100", salary=15000, birthdate="1975-01-10", department="dep1")
_employees = [_empl1, _empl2, _empl3, _empl4, _empl5, _empl6]
class TestCompany(TestCase):
    def setUp(self):
        for empl in list(companyInstance.getAllEmployees()):
            companyInstance.fireEmployee(empl.id)
        for empl in _employees:
            companyInstance.hireEmployee(empl)
                
            
    def test_get_all_employees(self):
        self.assertEqual(_employees,sorted(companyInstance.getAllEmployees()))
    def test_adding_existed_employee(self) :
        with self.assertRaises(EmployeeAlreadyExists) :
            companyInstance.hireEmployee(_empl1) 
    def test_remove_not_existed_employee(self) :
        with self.assertRaises(EmployeeNotFoundError) :
            companyInstance.fireEmployee("1111111111") 
    def test_get_employees_department(self):
        self.assertEqual([_empl1, _empl2], list(companyInstance.getEmployeesByDepartment("dep1")))
        companyInstance.hireEmployee(_emplForAdd)
        self.assertEqual([_empl1, _empl2, _emplForAdd], list(companyInstance.getEmployeesByDepartment("dep1")))
        companyInstance.fireEmployee(_empl2.id)
        self.assertEqual([_empl1,  _emplForAdd], list(companyInstance.getEmployeesByDepartment("dep1")))
        self.assertEqual([], list(companyInstance.getEmployeesByDepartment("dep1000")))
    def test_get_employees_salary(self) :
        self.assertEqual([_empl2], list(companyInstance.getEmployeesBySalary(11000, 17000))) 
        companyInstance.hireEmployee(_emplForAdd)  
        self.assertEqual([_empl2, _emplForAdd], list(companyInstance.getEmployeesBySalary(11000, 17000))) 
        companyInstance.fireEmployee(_empl2.id) 
        self.assertEqual([ _emplForAdd], list(companyInstance.getEmployeesBySalary(11000, 17000))) 
        self.assertEqual([], list(companyInstance))     
    def test_get_employees_age(self) :
        self.assertEqual([_empl1], list(companyInstance.getEmployeesByAge(50,70)))    
        companyInstance.hireEmployee(_emplForAdd) 
        self.assertEqual([_empl1,_emplForAdd], list(companyInstance.getEmployeesByAge(50,70)))
        companyInstance.fireEmployee(_empl1.id)    
        self.assertEqual([_emplForAdd], list(companyInstance.getEmployeesByAge(50,70)))
        self.assertEqual([],list(companyInstance.getEmployeesByAge(60,70)) )