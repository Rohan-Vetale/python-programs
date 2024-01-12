"""
@Author: Rohan Vetale

@Date: 2024-01-12 17:15

@Last Modified by: Rohan Vetale

@Last Modified time: 2024-01-12 17:15

@Title : Employee Wage Computation Problems with logger
"""
import random
import logging

logging.basicConfig(filename='employee_log.log',level=logging.DEBUG,format='%(asctime)s %(message)s',datefmt='%m:%d:%y '
                                '%I:%M:%S %p')
logger = logging.getLogger(__name__)

class Employee:
    def __init__(self, emp_name, wage_per_hours, max_working_day, max_working_hours):
        self.wage_per_hrs = wage_per_hours
        self.max_working_days = max_working_day
        self.max_working_hrs = max_working_hours
        self.employee_name = emp_name
        self.total_wage = 0

    def employee_wage_calculation(self):
        """
        Description: calculation of Employee Wage Computation Problem.
        Parameter: None
        Return:None
        """
            # print("Welcome to Employee Wage Computation Program on Master Branch")
        emp_working_hrs = 0
        emp_working_days = 0
        while emp_working_hrs < self.max_working_hrs and emp_working_days < self.max_working_days:
            empType = random.randint(0, 2)
            working_hours = 0
            match empType:
                case 0:
                    working_hours = 0
                    # print("Employee is not present")
                case 1:
                    # print("Employee is present and working Part time")
                    working_hours = 4
                case 2:
                    # print("Employee is present and working Full time")
                    working_hours = 8
            emp_working_hrs += working_hours
            self.total_wage += working_hours * self.wage_per_hrs
            emp_working_days += 1
        # print(f"Max working Days: {emp_working_days}")
        # print(f"Total working hours of an employee is: {emp_working_hrs}")
        # print(f"Total working days of an employee is: {self.total_wage}")


class Company:
    def __init__(self, company_name):
        self.comp_name = company_name
        self.employee_dict = {}

    def add_employee(self, employee_obj: Employee):
        """
        Description: This function add the employee.
        Parameter: employee class object
        Return:None
        """

        self.employee_dict.update({employee_obj.employee_name: employee_obj})


    def employee_details(self):
        """
        Description: This function returns all employee details.
        Parameter: None
        Return:None
        """
        for key, value in self.employee_dict.items():
            logger.info(f"Name: {key} Total Wage: {value.total_wage} Company Name: {self.comp_name} ")

    def get_employee(self, employee_name):
        """
        Description: This function get the employee from the employee dictionary.
        Parameter: String
        Return:None
        """
        self.employee_dict.get(employee_name)
        logger.info(f"{employee_name} Employee is fetched!!")

    def update_employee(self, employee_name):
        """
        Description: This function update the employee.
        Parameter: String
        Return:None
        """
        employee_obj: Employee = self.employee_dict.get(employee_name)
        if employee_obj:
            employee_obj.employee_wage_calculation()
            self.employee_dict.update({employee_name: employee_obj})
            logger.info(f"{employee_name} UpDated!!")
        else:
            logger.info("Employee is not Found!!")


    def delete_employee(self, employee_name):
        """
        Description: This function delete the employee from the employee dictionary.
        Parameter: String
        Return:None
        """
        employee_boj: Employee = self.employee_dict.get(employee_name)
        if employee_boj:
            self.employee_dict.pop(employee_name)
            logger.info("deleted!!")
        else:
            logger.info("Employee is not Found!!")


class MultipleCompany:
    def __init__(self):
        self.company_dict = {}


def main():
    multi_company_obj = MultipleCompany()
    try:
        while True:
            print(
                "choice 1 to add employee\nchoice 2 to get all details of employees\nchoice 3 to get an employee from a company\n"
                "choice 4 for update an employee from a company\nchoice 5 for delete an employee from a company\nchoice 6 for all "
                "company details\nchoice 7 to get company\nchoice 8 for delete company\nchoice 9 to get all employee "
                "details in a company\nchoice 10 to exit")
            user_choice = int(input("Enter your choice: "))
            match user_choice:
                case 1:
                    comp_name = input("Enter your company name: ")
                    company_obj = multi_company_obj.get_company(comp_name)
                    if company_obj is None:
                        company_obj = Company(comp_name)
                    employee_name = input("Enter the emp name: ")
                    wage_per_hrs = int(input("Enter wage per Hours: "))
                    max_working_days = int(input("Enter Max working Days: "))
                    max_working_hrs = int(input("Enter Max working Hours: "))
                    employee_obj = Employee(employee_name, wage_per_hrs, max_working_days, max_working_hrs)
                    employee_obj.employee_wage_calculation()
                    company_obj.add_employee(employee_obj) 
                    multi_company_obj.add_company(company_obj)
                case 2:
                    comp_name = input("Enter your company name: ")
                    company_obj = multi_company_obj.get_company(comp_name)
                    if company_obj is None:
                        pass
                    company_obj.employee_details()  
                case 3:
                    employee_name = input("Enter the emp name: ")
                    comp_name = input("Enter your company name: ")
                    company_obj = multi_company_obj.get_company(comp_name)
                    if company_obj is None:
                        pass
                    company_obj.get_employee(employee_name) 
                case 4:
                    employee_name = input("Enter the emp name: ")
                    comp_name = input("Enter your company name: ")
                    company_obj = multi_company_obj.get_company(comp_name)
                    if company_obj is None:
                        logger.info('Company not found!!')
                    company_obj.update_employee(employee_name) 
                case 5:
                    employee_name = input("Enter the emp name: ")
                    comp_name = input("Enter your company name: ")
                    company_obj = multi_company_obj.get_company(comp_name)
                    if company_obj is None:
                        pass
                    company_obj.delete_employee(employee_name) 
                case 6:
                    multi_company_obj.all_comp_details()  
                case 7:
                    comp_name = input("Enter company name: ") 
                    multi_company_obj.get_company(comp_name)
                case 8:
                    comp_name = input("Enter company name: ")
                    multi_company_obj.remove_company(comp_name)  
                case 9:
                    comp_name = input("Enter your company name: ")
                    company_obj = multi_company_obj.get_company(comp_name)
                    if company_obj is None:
                        pass
                    multi_company_obj.get_company_with_all_employee(company_obj.comp_name)
                case 10:
                    break
    except Exception as e:
        logger.exception(e)


if __name__ == '__main__':
    main()