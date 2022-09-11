import random
import time

"""
Use naive search to go through each index
@param l: list
@param trial_number: number we are looking for 
"""

#naive search: scan entire list and ask if its equal to the target
#if yes, return the index
# if no, then return -1



def naive_search(l, trial_number):
    # example list = [1,3,10,12]
    for i in range(len(l)):
        if (l[i] == trial_number):
            return i
    return -1


#binary search uses divide and conquer!
#List MUST be sorted.
"""
Using binary search to only search key target areas for our trial_number
@param l = list
@trial_number = number we are looking for
@low, high are both indices.
"""
def binary_search(l,trial_number, low =None, high=None): #Low and High are lowest indices to the highest indices that we search.
    # example l = [1,3,5,10,12]
    # If target is 10
    if low is None:
        low =0
    if high is None:
        high = len(l)-1 #Last index by default

    if high < low:
        return -1 #Target is not in the list

    midpoint = (low + high) // 2 #index is an integer

    if l[midpoint] == trial_number:
        return midpoint
    elif trial_number < l[midpoint]:
        # If our tried number index is less than the midpoint then we search again from
        # index = 0 to midpoint of (0,index = 1 less than the midpoint.)
        # then again if trial_number < l[midpoint], once again we search again. This time midpoint is again averaged of 0 and previous midpoint-1
        # This pattern continues given trial_number < l[midpoint]
        return binary_search(l, target, low, midpoint-1)
    else:
        # target > l[midpoint]
        # if our tried number index is more than the midpoint then we search again from
        # index = midpoint + 1 to  average of (midpoint +1, last index). This pattern repeats with each recusive call. 
        # as long as trial_number > l[midpoint]
        
        return binary_search(l, target, midpoint+1, high)


if __name__=='__main__':
    L = [4,10,22,37,10000]
    trialNum= 22
    print(naive_search(L, trialNum))
    print(binary_search(L, trialNum))

 
    #Timing analysis
    # build a sorted length of length 20000
    length = 20000
    sorted_list = set()
    while len(sorted_list) < length:
        sorted_list.add(random.randint(-3*length, 3*length))
    sorted_list =sorted(list(sorted_list))

    s = time.time()
    for target in sorted_list:
        naive_search(sorted_list, target)
    e = time.time()
    print("Naive search time took:", (e-s)/length, "seconds")

    s =time.time()
    for target in sorted_list:
        binary_search(sorted_list, target)
    e= time.time()
    print("Binary search time took: ", (e - s)/length, "seconds")



