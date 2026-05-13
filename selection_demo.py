
from selection_sort import selection_sort
import selection_sort as s_sort

import sys

numbers=[]




for i in range(1,len(sys.argv)):
    numbers.append(float(sys.argv[i]))

print(f'Numbers before sorting',numbers)

x=selection_sort(numbers)

print(f'numbers after sorting',x)

for i in range(1,len(sys.argv)):
    numbers.append(float(sys.argv[i]))

print(f'Number before sorting\n{numbers}')

x=s_sort.selection_sort(numbers)

print(f'Number after sorting\n{numbers}')


