'''

@Author: Rohan Vetale

@Date: 2023-01-02 16:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2023-01-02 16:00:30

@Title : Flip Coin and print percentage of Heads and Tails

'''


import random
while True:
    num_of_events = int(input("Enter the number of times you want to flip a coin : "))
    if num_of_events > 0:
        break
    else:
        print("Please enter a positive number")
#initializing counts and events
current_event = 0
head_counts = 0
tail_counts = 0

#seeking user input for number of events
while True:
    
    if current_event == num_of_events:
        break
    else:
        coin_val = random.random()
        if coin_val < 0.5 :
            tail_counts += 1
            
        else:
            head_counts += 1
        current_event += 1

#calculating the percentage of heads with respect to tails
try :
    print("Tail counts : ", tail_counts, "Head counts : ", head_counts)
    percent_val = (head_counts / num_of_events) * 100
    print("Percentage of heads versus tails is : ", percent_val)
    print("Percentage of tails versus heads is ", 100-percent_val)
except Exception as e:
    print("Error occured please try again ") 
    print("Exception : " , e)   
