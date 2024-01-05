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
     

try:
    if is_present() :
        print("Employee is present today")
        daily_wage = calc_daily_wage(wg_per_hr=20, hr_per_day=8)
        print(f"Employee's daily wage is {daily_wage}")
    else:
        print("Employee is absent today")
        
except Exception as e:
    print(f"Exception occured {e} please try again")
    