'''

@Author: Rohan Vetale

@Date: 2023-01-02 16:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2023-01-02 16:00:30

@Title : Take a 4 digit numeric user input and print whether it is a leap year or not

'''


while True:
    input_year = input("Enter the year to check whether it is a leap year or not : ")
    #check if it is less than 4 digits or not
    if len(input_year) < 4:
        print("Please enter the year in 4 digits format !")
    else:
        #check if it is a leap year or not
        input_year = int(input_year)
        if input_year % 4 == 0 and (input_year % 100 or input_year % 400):
            print("Entered year " , input_year ," is a leap year")
        else:
            print("Entered year " , input_year ," is not a leap year")
        break
