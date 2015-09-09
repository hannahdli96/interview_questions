# Implement binary search on a sorted array of integers. Does this change for non sorted?
# The array MUST be sorted in order for this to work. It can be sorted backwards, though, so long as you adjust your code.

"""Return whether or not it's in the array:
>>> a = [1,2,3,4,5]
>>> bin_search(a,3)
'yes, it is in the array'
>>> b = [1,2,3,4,5,6,7]
>>> bin_search(b,8)
'no, it is not in the array'
"""

def bin_search(arr, x): 
	mid = arr[len(arr)//2]
	mid_index = len(arr)//2
	if len(arr) == 1 & arr[0] != x: 
		return "no, it is not in the array"
	elif x == mid:
		return "yes, it is in the array"
	elif x > mid: 
		return bin_search(arr[mid_index:],x)
	elif x < mid:
		return bin_search(arr[:mid_index],x)