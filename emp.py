import random


class Employee:
    def __init__(self, emp_name, wage_per_hours, max_working_day, max_working_hours):
        self.wage_per_hrs = wage_per_hours
        self.max_working_days = max_working_day
        self.max_working_hrs = max_working_hours
        self.employee_name = emp_name
        self.total_wage = 0

    def employee_wage_calculation(self):
        """
        Description: implementation of Employee Wage Computation Problem.

        Parameter: None

        Return:None
        """
        print("Welcome to Employee Wage Computation Program on Main Branch")
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


if __name__ == '__main__':
    employee_name = input("Enter the emp name: ")
    wage_per_hrs = int(input("Enter wage per Hours: "))
    max_working_days = int(input("Enter Max working Days: "))
    max_working_hrs = int(input("Enter Max working Hours: "))
    employee_obj = Employee(employee_name, wage_per_hrs, max_working_days, max_working_hrs)
    employee_obj.employee_wage_calculation()
    print(f"{employee_obj.total_wage}")