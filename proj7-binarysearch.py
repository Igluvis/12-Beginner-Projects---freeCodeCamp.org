def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1

def binary_search(l, target):
    # list not empty
    if l:
        # middle index
        middle = len(l)//2
    
        # found target
        if l[middle] == target or len(l) == 1:
            return 1

        # target smaller than middle
        elif l[middle] > target:
            return binary_search(l[:middle], target) + 1
        
        # target greater than middle
        else:
            return binary_search(l[middle + 1:], target) + 1

    return -1

list = [i for i in range(100)]
target = 45

print(naive_search(list, target))
print(binary_search(list, target))