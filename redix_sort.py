## python version: python 3.6.0, require numpy version >= 1.14.0

### redix sorting method
import numpy as np


def get_dig_num(num, n = 1):
    """
    this function gets the n-th digit of a number
    For example, 123 has 0th digit 3, 1st digit 2 and 2nd digit 1

    :params[in]:num, the number to get its n-th digit
    :params[out]:n-th digit,
    """
    digit = num//10**n%10 # this is the n-th digit, 0-indexed
    return digit

## example
num = 1025
get_dig_num(num, 0)
get_dig_num(num, 1)
get_dig_num(num, 2)
get_dig_num(num, 3)
get_dig_num(num, 4) ## 0 if doesn't have 4-th digit

def myredix(list_to_sort):
    """
    :params:[in],list_to_sort,list
    :params:[out],sorted_list
    """
    number_digits = int(np.max(np.log10(np.array(list_to_sort)))) +1
    ## loop over each digit
    for n in range(number_digits):
        bucket = [[] for i in range(10)] # all buckets to hold numbers
        ## loop over all numbers
        for it in list_to_sort:
            ## get the n-th digit number and put this number to
            ## corresponding bucket
            bucket[get_dig_num(it, n)].append(it)
        ## clear the list
        list_to_sort.clear()
        ## rearrange the buckets
        # lsit comprehension to concatenate numbers in all buckets
        [list_to_sort.extend(it) for it in bucket]
    ## return the sorted array from small to large
    sorted_list = list_to_sort
    return sorted_list

### examples
l1 = [1, 4, 5, 21, 65, 60, 1000,2000,4,21]
myredix(l1)

l1 = [0, 4, 5, 11, 65, 60, 10005,20400,41,21]
myredix(l1)
