from selection_sort import selection_sort

import sys

numbers=[]




for i in range(1,len(sys.argv)):
    numbers.append(float(sys.argv[i]))

print(f'Numbers before sorting',numbers)

x=selection_sort(numbers)

print(f'numbers after sorting',x)