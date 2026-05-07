def factorial_of_number(number):
    if number<0:
        return "Factorial does not exist for negative numbers"
    elif number == 0 or number == 1:
        return 1
    else:
        return number * factorial_of_number(number-1)   
input_number=int(input("Enter the number which factorial you want to find:"))
print(f'The factorial of {input_number} is {factorial_of_number(input_number)}')