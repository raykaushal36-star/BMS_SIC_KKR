def merge(numbers, low, high, mid):
    temp = []
    i = low
    j = mid + 1
    
    while i <= mid and j <=high:
        if numbers[i] < numbers[j]:
            temp.append(numbers[i])
            i +=1
        else:
            temp.append(numbers[j])
            j +=1
    while i <= mid:
        temp.append(numbers[i])
        i+=1
    while j <= high:
        temp.append(numbers[j])
        j +=1
    for i in range(len(temp)):
        numbers[low + i] = temp[i]
