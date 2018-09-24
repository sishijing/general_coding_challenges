"""
find the maximum sum of subarrays of an input array
If the input array has all positive elements, then the maximum
will be the sum of whole array. If it has negative values, the maximum
will be the sum of one certain subarray.

The following approach uses the idea that the sum of an subarray 
starting from i-th element and ending at j-th element equals to
the partial sum F(j) - F(i), where F(i) is the partial sum of the
array ending at i-th element.
"""


def findMaxSubarray(arr):
    """
    params:
      arr -- input array
    returns:
      maxSub -- maximum sum of subarray
      startInd -- starting index
      endInd -- ending index in pythonic way, not included
    """
    part_sum = 0 ## partial sum sequence
    len0 = len(arr) ##length of input array
    tmp_max = part_sum # temporary maximum of subarrays
    # For an empty subarray, the sum is zero
    tmp_min = min(0, part_sum) # temp. mini. of partial sum
    startInd, endInd, newStart = 0,0,0
    ## for loop
    for i in range(0,len0):
        part_sum += arr[i]
        ## if current partial sum is less than temporary min.
        if part_sum < tmp_min:
            tmp_min = part_sum
            newStart = i+1
        pos_max = part_sum - tmp_min # possible maximum
        if pos_max > tmp_max:
            tmp_max = pos_max
            endInd,startInd = (i+1),newStart
    return tmp_max, startInd, endInd

###### test the code
## example 1:
a = [1,2,3,-4,-1,9,1]
res, start, end = findMaxSubarray(a)
res
sum(a[start: end])
## example 2:
a = [1]
res, start, end = findMaxSubarray(a)
res
sum(a[start: end])
## example 3:
a = [1,2]
res, start, end = findMaxSubarray(a)
res
sum(a[start: end])

## example 4
a = [-1,-2,2.2,3.4,5.0,-8.9,-1.0]
res, start, end = findMaxSubarray(a)
res
sum(a[start: end])

## example 5
a = [2.2,3.4,2.0,-8.9,-11.0, -10]
res, start, end = findMaxSubarray(a)
res
sum(a[start: end])

## example 6
a = [1.0,2.0,-5.0,4.0,-3.0,2.0,6.0,-5.0, -1.0]
res, start, end = findMaxSubarray(a)
res
sum(a[start: end])

