'''
selection sort

'''
def selection_sort(numbers):
    for i in range(len(numbers)-1):
        for j in range(i+1,len(numbers)):
            if numbers[i] > numbers[j]:
                numbers[j],numbers[i] = numbers[i],numbers[j]
    return numbers
            
