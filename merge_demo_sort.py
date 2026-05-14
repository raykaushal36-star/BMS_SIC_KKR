import sys

import merge_sort as ms

list = [float(value) for value in sys.argv[1:]]

print(f"Before sorting: {list}")

ms.merge_sort(list, 0, len(list) - 1)

print(f"After sorting: {list}")
