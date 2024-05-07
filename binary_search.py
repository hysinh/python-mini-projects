# Code by Kylie Ying, tutorial: https://www.youtube.com/watch?v=8ext9G7xspg

# Implementation of binary search algorithm!

#naive search: scan the entire list and ask if it's equal to the target
#if yes, return the index
#if no, then return -1

# CODE NOT WORKING 


def naive_search(l, target):
    # example l = [1, 3, 10. 12]
    for i in range(len(l)):
        if l[i] == target:
            return i
    return -1


# binary search uses divide and conquer!
# we will leverage the fact that our list is SORTED
def binary_search(l, target):
    # example = l [1, 3, 5, 10, 12]
    midpoint = len(l) // 2 # 2 //= floor division

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l[midpoint - 1], target)
    else: 
        # target > l[midpoint]
        return binary_search(l[midpoint + 1], target)
    

# binary search with low and high arguments (limits)
def binary_search_low_high(l, target, low=None, high=None):
    if low is None:
        low = 0
    if high is None:
        high = len(l) -1

    if high < low:
        return -1

    
    # example = l [1, 3, 5, 10, 12]
    midpoint = (len(l)) // 2 # 2

    if l[midpoint] == target:
        return midpoint
    elif target < l[midpoint]:
        return binary_search(l, target, low, midpoint-1)
    else: 
        # target > l[midpoint]
        return binary_search(l, target, midpoint+1, high)
    

if __name__=='__main__':
    l = [1, 3, 5, 10, 12]
    target = 10
    print(naive_search(l, target))
    print(binary_search(l, target))
    