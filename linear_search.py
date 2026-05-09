'''read size of the list from user ,say N
Read N number of elements of the list
Read the search element from the User
Ask the function sequentially_search(serarch_elements,elements) to search the elements )
The function will return the index of 1st occurence of the elements
else -1
'''
def sequentially_search(search_element,elements):
    for i in range(len(elements)):
        if elements[i]==search_element:
            return i
    return -1
        



input_size=int(input("Enter size of the list:"))

elements=[]

print(f"Enter the {input_size} elements of the list:")
for i in range(input_size):
    element=float(input())
    elements.append(element)

print('user given elents are:',elements)
search_element=float(input("Enter the serach elements:"))
search_index=sequentially_search(search_element,elements)
if search_index == -1:
    print(f"{search_element} not found")

