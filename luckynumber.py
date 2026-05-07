

'''
Algorithm:
Read the input number say N
    Go on finding the sum of digit of given number N
    if
        sum  is not singlen  digit number, then repeat step 1
    else
        print the sum o/p


input_number = 789
input_number = input_number // 10 #78
789 % 10  #9
'''

#input_number=input
input_number=int(input("Enter the number:"))
print(f'Number you input is {input_number}')
sum_of_digit=0
while input_number != 0:
    rem=input_number % 10
    input_number=input_number//10
    sum_of_digit+=rem
    if sum_of_digit >9 and input_number == 0:
        input_number = sum_of_digit
        sum_of_digit = 0
print(f"You lucky number is {sum_of_digit}")

