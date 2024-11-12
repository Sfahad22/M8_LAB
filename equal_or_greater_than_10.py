# Shaik Fahad
# Nov 12, 2024

# Problem 2, 
# This program ask user for 2 numbers and check if that number is equal or greater or less than 10.  



def check_sum():
    input1 = int(input("Enter the first number: "))
    input2 = int(input("Enter the second number: "))
        
    total = input1 + input2
    
    if total > 10:
        print("The sum is greater than 10.")
    elif total < 10:
        print("The sum is less than 10.")
    else:
        print("The sum is equal to 10.")

check_sum()