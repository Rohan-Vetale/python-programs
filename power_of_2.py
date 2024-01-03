'''

@Author: Rohan Vetale

@Date: 2023-01-03 10:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2023-01-03 18:00:30

@Title : Print a table of 2^N where N is user input integer

'''

while True:
    power_num = int(input("Enter a power number between 0 and 30 : "))
    if power_num >= 0 and power_num < 31:
        for i in range(0,power_num+1):
            print("2 ^ ", i, " = ", 2**i)
        break
    else:
        print("Please enter a number between 0 and 30 !")
        
