# Find pairs in an integer array whose sum is equal to 10. Also do it in linear time
# Assume everything in the array is an integer

# Runs in O(n^2)
# This prints you all of them

"""
>>> arr1 = [0,1,2,3,4,5,6,7,8,9,10]
>>> int_sum_to_10(arr1)
0 10
1 9
2 8
3 7
4 6
"""

def int_sum_to_10(arr):
	last = len(arr) - 1
	for i in range(len(arr) //2): 
		for j in range(len(arr) //2):
			if arr[i] + arr[last - j] == 10:
				print str(arr[i]) + " " + str(arr[last - j])
