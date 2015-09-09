# Find the common elements of 2 arrays

# 

"""Runs in O(xy) time, where x and y are the lengths of the two arrays
>>> arr1 = [1,2,3,4,5,6]
>>> arr2 = [6,7,8,9,10,11]
>>> common_el(arr1, arr2)
[6]
>>> arr3 = [1,2,3]
>>> arr4 = [4,5]
>>> common_el(arr3, arr4)
[]
"""
def common_el(arr1, arr2):
	result = []
	for i in arr1: 
		for j in arr2:
			if (i == j) & (i not in result):
				result.append(i)
	return result