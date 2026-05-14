'''
Go to mid element of the list and check if it is the search
If yes,
       then the search can stopped
If not,
       then check if element is less than the mid element (i.e if the element is in first half od the list)
       if yes,
              then set the saerch area to 1st half of the list
        if not,
               set the search area to 2nd half
        Repeat the above steps until the search area is empty or the element is found



'''
import sys
import binary_search


input_numbers =[]
print(f'User given elements are')
for i in range(1,len(sys.argv)):
    input_numbers.append(float(sys.argv[i]))

print(f'user given elents are\n',input_numbers)

search_element=float(input('Enter the element to be searched:'))
search_index=binary_search(search_element,input_numbers)
if search_index == -1:
    print(f"{search_element} not found")
