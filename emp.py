import random
import logging

logging.basicConfig(filename='employee_log.log', level=logging.DEBUG, format='%(asctime)s %(message)s',
                    datefmt='%m:%d:%y %I:%M:%S %p')
logger = logging.getLogger(__name__)

class Employee:
    def __init__(self, employee_name, wage_per_hour, max_working_day, max_working_hours):
        self.wage_per_hrs = wage_per_hour
        self.max_working_days = max_working_day
        self.max_working_hrs = max_working_hours
        self.employee_name = employee_name
        self.total_wage = 0

    def employee_wage_implementation(self):
        emp_working_hrs = 0
        emp_working_days = 0
        while emp_working_hrs < self.max_working_hrs and emp_working_days < self.max_working_days:
            emp_type = random.randint(0, 2)
            working_hours = 0
            match emp_type:
                case 0:
                    working_hours = 0
                case 1:
                    working_hours = 4
                case 2:
                    working_hours = 8
            emp_working_hrs += working_hours
            self.total_wage += working_hours * self.wage_per_hrs
            emp_working_days += 1

class Company:
    def __init__(self, company_name):
        self.company_name = company_name
        self.employee_dict = {}

    def add_employee(self, employee_obj: Employee):
        self.employee_dict.update({employee_obj.employee_name: employee_obj})

    def employee_details(self):
        for employee_name, employee_data in self.employee_dict.items():
            logger.info(f"Employee Name: {employee_name} Employee Data: {employee_data.total_wage}")

def main():
    company_dict = {}
    try:
        while True:
            print(
                "choice 1 for add employee\nchoice 2 for all details of employee\nchoice 3 to get an item from dictionary\n"
                "choice 4 for update an item of dictionary\nchoice 5 for delete an item of dictionary\nchoice 6 for all "
                "company details\nchoice 7 to get company\nchoice 8 for delete company\nchoice 9 to get all employee "
                "details in a company\nchoice 10 to exit")
            user_choice = int(input("Enter your choice: "))
            match user_choice:
                case 1:
                    company_name = input("Enter your company name: ")
                    company_obj = company_dict.get(company_name)
                    if company_obj is None:
                        company_obj = Company(company_name)
                        company_dict[company_name] = company_obj
                    employee_name = input("Enter the employee name: ")
                    wage_per_hour = int(input("Enter wage per Hours: "))
                    max_working_days = int(input("Enter Max working Days: "))
                    max_working_hours = int(input("Enter Max working Hours: "))
                    employee_obj = Employee(employee_name, wage_per_hour, max_working_days, max_working_hours)
                    employee_obj.employee_wage_implementation()
                    company_obj.add_employee(employee_obj)
                case 2:
                    company_name = input("Enter your company name: ")
                    company_obj = company_dict.get(company_name)
                    if company_obj is not None:
                        company_obj.employee_details()
                case 3:
                    employee_name = input("Enter the employee name: ")
                    company_name = input("Enter your company name: ")
                    company_obj = company_dict.get(company_name)
                    if company_obj is not None:
                        employee_obj = company_obj.employee_dict.get(employee_name)
                        if employee_obj is not None:
                            logger.info(f"Employee Name: {employee_name} Employee Data: {employee_obj.total_wage}")
                case 4:
                    employee_name = input("Enter the employee name: ")
                    company_name = input("Enter your company name: ")
                    company_obj = company_dict.get(company_name)
                    if company_obj is not None:
                        employee_obj = company_obj.employee_dict.get(employee_name)
                        if employee_obj is not None:
                            logger.info(f"Updating employee data for {employee_name}")
                            employee_obj.employee_wage_implementation()
                case 5:
                    employee_name = input("Enter the employee name: ")
                    company_name = input("Enter your company name: ")
                    company_obj = company_dict.get(company_name)
                    if company_obj is not None:
                        company_obj.employee_dict.pop(employee_name, None)
                        logger.info(f"Deleted employee {employee_name}")
                case 6:
                    for company_name, company_obj in company_dict.items():
                        logger.info(f"Company Name: {company_name} Company Data: {company_obj.employee_dict}")
                case 7:
                    company_name = input("Enter company name: ")
                    company_obj = company_dict.get(company_name)
                    if company_obj is not None:
                        logger.info(f"Company Name: {company_name} Company Data: {company_obj.employee_dict}")
                case 8:
                    company_name = input("Enter company name: ")
                    company_dict.pop(company_name, None)
                    logger.info(f"Deleted company {company_name}")
                case 9:
                    company_name = input("Enter your company name: ")
                    company_obj = company_dict.get(company_name)
                    if company_obj is not None:
                        for employee_name, employee_obj in company_obj.employee_dict.items():
                            logger.info(f"Employee Name: {employee_name} Employee Data: {employee_obj.total_wage}")
                case 10:
                    break
    except Exception as e:
        logger.exception



if __name__ == '__main__':
    main()
