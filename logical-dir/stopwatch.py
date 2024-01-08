'''

@Author: Rohan Vetale

@Date: 2023-01-04 16:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2023-01-04 16:00:30

@Title : Simulate a real life stopwatch which shows elapsed time

'''
from datetime import timedelta
import time


def start_stopwatch():
    """
        Description:
        This function is used to start the stopwatch

        Parameter:
        None

        Return:
        It does not return anything but prints the elapsed time
    """
    #define the stopwatch function
    input("Press Enter to start the stopwatch...")
    start_time = time.time()
    input("Press Enter to stop the stopwatch...")
    end_time = time.time()
    elapsed_time = end_time - start_time
    formatted_time = str(timedelta(seconds=round(elapsed_time)))
    print(f"Elapsed time is {formatted_time}")

#call the function
start_stopwatch()



