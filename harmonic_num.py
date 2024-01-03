'''

@Author: Rohan Vetale

@Date: 2023-01-03 10:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2023-01-03 18:00:30

@Title : Print a table of 2^N where N is user input integer

'''

while True:
    input_n = int(input("Enter N to find it's nth harmonic number : "))
    harm_num = 0
    if input_n > 0 :
        for i in range(1,input_n+1):
            harm_num += (1 / i)
            
        print(f"Nth harmonic of {input_n} is {harm_num}")
        break
    else:
        print("Enter a positive number")