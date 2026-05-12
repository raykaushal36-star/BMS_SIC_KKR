import quick_sort as qt
import sys

numbers = []


numbers = [int(value) for value in sys.argv[1:] ]

print(f'numbers before sorting:\n{numbers}')

qt.quick_sort(numbers, 0, len(numbers)-1)

print(f'Numbers after sorting:\n{numbers}')