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

try:
    if is_present() :
        print("Employee is present today")
        if part_or_full() == 1:
            daily_wage = calc_daily_wage(wg_per_hr=20, hr_per_day=4)
            wage_type = "Part time"
        else:
            daily_wage = calc_daily_wage(wg_per_hr=20, hr_per_day=8)
            wage_type = "Full time"
        print(f"Employee's daily wage is {daily_wage} as employee is {wage_type}")
    else:
        print("Employee is absent today")
        
except Exception as e:
    print(f"Exception occured {e} please try again")
    