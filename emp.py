'''

@Author: Rohan Vetale

@Date: 2023-01-05 16:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2023-01-05 16:00:30

@Title : Employee wage with Use Cases


'''
import random

def is_present():
    """
        Description:
        This function is used to tell whether the employee is present or not

        Parameter:
        None

        Return:
        It returns a boolean value True or False based on random.choice()
    """
    
    return random.choice([True, False])

def calc_daily_wage(wg_per_hr, hr_per_day):
    """
        Description:
        This function is used to calculate daily wage of an employee

        Parameter:
        wg_per_hr : It is employee's per hour wage
        hr_per_day : It is employee's per day working hours        

        Return:
        It returns daily wage of employee as integer value
    """   
    daily_wage = hr_per_day * wg_per_hr
    return daily_wage

def part_or_full():
    """
        Description:
        This function is know whether the employee is part time or full time

        Parameter:
        None

        Return:
        It returns an Integer value 1 or 2, for part time or full time
    """
    return random.randint(1,2)   

#initializing monthly wage
monthly_wage = 0
working_days = 20
emp_present = 0

try:
    for day in range(working_days):
        if is_present() :
            #employee is present
            emp_present += 1
            match part_or_full():
                case 1:
                    #When employee is part time
                    daily_wage = calc_daily_wage(wg_per_hr=20, hr_per_day=4)
                case 2:
                    #When employee is full time
                    daily_wage = calc_daily_wage(wg_per_hr=20, hr_per_day=8)
            monthly_wage += daily_wage
        else:
            #employee is absent
            monthly_wage += 0
            
            
except Exception as e:
    print(f"Exception occured {e} please try again")

print(f"Employee's monthly wage is {monthly_wage} $ for a month of {working_days} days, employee was present for {emp_present} days")
    