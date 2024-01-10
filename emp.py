'''

@Author: Rohan Vetale

@Date: 2023-01-05 16:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2023-01-10 16:00:30

@Title : Employee wage with Use Cases


'''

import random


class Worker:
    def __init__(self, name, hourly_wage, max_work_days, max_work_hours):
        self.hourly_wage = hourly_wage
        self.max_work_days = max_work_days
        self.max_work_hours = max_work_hours
        self.worker_name = name
        self.total_earnings = 0

    def calculate_wage(self):
        """
        Description: Implementation of Staff Wage Computation.

        Parameter: None

        Return: None
        """
        print("Welcome to Staff Wage Computation Program on Main Branch")
        work_hours = 0
        work_days = 0
        while work_hours < self.max_work_hours and work_days < self.max_work_days:
            work_type = random.randint(0, 2)
            hours_worked = 0
            match work_type:
                case 0:
                    hours_worked = 0
                    # print("Employee is not present")
                case 1:
                    # print("Employee is present and working Part time")
                    hours_worked = 4
                case 2:
                    # print("Employee is present and working Full time")
                    hours_worked = 8
            work_hours += hours_worked
            self.total_earnings += hours_worked * self.hourly_wage
            work_days += 1
        # print(f"Max working Days: {work_days}")
        # print(f"Total working hours of an employee is: {work_hours}")
        # print(f"Total working days of an employee is: {self.total_earnings}")


if __name__ == '__main__':
    worker_name = input("Enter the worker name: ")
    hourly_wage = int(input("Enter hourly wage: "))
    max_work_days = int(input("Enter Max working Days: "))
    max_work_hours = int(input("Enter Max working Hours: "))
    worker_obj = Worker(worker_name, hourly_wage, max_work_days, max_work_hours)
    worker_obj.calculate_wage()
    print(f"{worker_obj.total_earnings}")
