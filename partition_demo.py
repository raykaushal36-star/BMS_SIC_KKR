import partition as pt
import sys

numbers = []


numbers = [int(value) for value in sys.argv[1:] ]

print(f'numbers before partition:\n{numbers}')

pt.partition_array(numbers)

print(f'Numbers after partition:\n{numbers}')