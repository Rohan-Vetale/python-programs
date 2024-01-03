'''

@Author: Rohan Vetale

@Date: 2023-01-02 16:00:30

@Last Modified by: Rohan Vetale

@Last Modified time: 2023-01-02 16:00:30

@Title : Use a given string template to concatenate user input and print output accordingly.

'''


#Taking user input
while True:
    user_name = input("Please enter your user_name : ")
    #Check whether the input is more than 3 characters
    if(len(user_name)>=3):
        #printing the output according to the given string template
        print("Hello "+ user_name +", How are you?")
        break
        #break if the user has entered a valid input
    else:
        #else ask the user to enter a valid input again
        print("Please enter a valid user name with more than 3 characters length")
