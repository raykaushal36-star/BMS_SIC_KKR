import insertion_sort as ins_sort
import sys

numbers=[]

for i in range(1,len(sys.argv)):
    numbers.append(float(sys.argv[i]))
print('Numbers before sorting:\n',numbers)
x=ins_sort.insertion_sort(numbers)
print('Numbers after sortintg:',x)
