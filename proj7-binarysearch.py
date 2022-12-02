import random
import time

def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search_my_solution(l, target):
    # list not empty
    if l:
        # middle index
        middle = len(l)//2
    
        # found target
        if l[middle] == target:
            return 0

        # target smaller than middle
        elif l[middle] > target:
            return binary_search(l[:middle], target) + 1
        
        # target greater than middle
        else:
            return binary_search(l[middle + 1:], target) + 1

    return -1

def binary_search(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) - 1

    if high < low:
        return -1

    mid = (low + high) // 2

    if l[mid] == target:
        return mid
    elif l[mid] > target:
        return binary_search(l, target, low, mid-1)
    else:
        return binary_search(l, target, mid+1, high)

# list = [i for i in range(100)]
# target = 45

# print(naive_search(list, target))
# print(binary_search(list, target))

if __name__ == '__main__':
    length = 10000

    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    
    sorted_list = sorted(list(sorted_list))

    start = time.time()

    for target in range(length):
        naive_search(sorted_list, target)

    end = time.time()

    print('Naive search time: ', (end-start)/length)

    start = time.time()

    for target in range(length):
        binary_search(sorted_list, target)

    end = time.time()

    print('Binary search time: ', (end-start)/length)