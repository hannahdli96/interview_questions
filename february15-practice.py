### This is a compilation of the most helpful interview questions I saw during the fall-14 interview season
from __future__ import division
import random
from heapq import heappush, heappop
from time import time
from bisect import bisect_left
__author__ = "Paul Moulton"


"""
1. Write a function that takes a list of parenthesis and returns True if they match (are coherent).
   ex: 
   ["(", "{", "}", ")"] returns True
   ["(", "}", ")"] returns False

   the answer is below.

   *You can make this more advanced by taking in keys and generalizing the matching

2. Look up twitter interview questions on glassdoor and try them and understand the solutions!
	Very important. you might see repeats.

3. Write a function that chooses a server from a list with distributed random probability.

	input: list of server, weight tuples
	output: the name of a server

	example: [("server-1", 20), ("server-2", 5), ("server-3", 10)] -> Choose server-1 with 20/35 probability.

	*You can make this faster by binary searching for the server by searching on the sum.

4. Try the three_sums problem. Given a list of integers and a target sum, return a triple (three numbers in the list)
	that sums to that target sum.

	[1, 3, 6, 4, 8], target=15
	returns (3, 4, 8)

	This is well documented online. 

	*You can make this faster by using fast fourier transform method that checks for a target sum in nlogn time.


		Main Idea. Encode the array of elements into a polynomial where each term has a coefficient of 1 and each power is the element of the array. 
		Cube the list. Each element of the resulting polynomial will have a power 
		that is the result of adding three unique elements in the list. check if the result is the target.

		Pseudocode.
		def three_sum(array):
		    1. Make a polynomial out of the array where each element has a coefficient of 1
		     and a power that is the element of the array.
		    2. Cube the list by multiplying it by itself twice using FFT.
		    3. Check each term for the target in the exponent and return True if you find one,
		     otherwise return false

		Proof of Correctness. The algorithm can find whether or not you have three elements in your list that sum to the 0 because multiplying polynomials returns 
		a polynomial containing exponents of all the different ways to add the exponents together. Since we have formulated all the ways of adding the numbers together,
		 we can check if three numbers sum to zero by checking for zero exponents.

		Running Time. O(nlog(n))

		Justification. The algorithm will take two FFT multiplications that will take O(nlog(n)) and one linear check of the polynomial that will take O(n). 
		Therefore the algorithm runs in O(nlog(n))

5. Group words by anagrams. Given a list of words, output a list of words with anagrams grouped.
		
	This one is easy. 

	*You can make this faster by hashing the word into the dictionary instead of sorting.

6. Given a lowercase base 62 integer, return all of the possible base 62 integers possible
	input: int_62
	output: list of int_62s

	example: 3bq -> [3BQ, 3Bq, 3bQ, 3bq]

7. Implement an LRU cache. Accesses most recently used item in constant time.
http://www.cs.uml.edu/~jlu1/doc/codes/lruCache.html

8. Write atoi in C.

9. When would you use a binary search tree instead of a hashtable?


"""

def anagrams(words):
	output = dict()
	for word in words:
		sorted_word = str(sorted(word))
		if sorted_word in output:
			output[sorted_word].append(word)
		else:
			output[sorted_word] = [word]
	return sorted(output.values())


def match_p(par):
	"""
	Takes in a list of parenthesis and determines whether they match or not.

	input: a list of parenthesis
	output: boolean True if they match, False otherwise
	"""
	stack = []
	for item in par:
		if item == "(":
			stack.append(")")
		elif item == "{":
			stack.append("}")
		else:
			if not stack or stack.pop() != item:
				return False
	return True if not stack else False

def deenc(word):
	"""
	Given a base 62 integer coerced to lower case, return all the possible base 62 integers

	input: int_62
	output: list of int_62s

	example: 3bq -> [3BQ, 3Bq, 3bQ, 3bq]

	"""
	output = ['']
	chars = xrange(ord('a'), ord('z'))
	for char in word:
		newoutput = []
		for item in output:
			if ord(char) in chars:
				newoutput.append(item + char.upper()) 
			newoutput.append(item + char)
		output = newoutput
	return output

def weighted_prob(servers):
	"""
	Given a list of servers, choose one from the list with distributed random probability.

	input: list of server, weight tuples
	output: the name of a server

	example: [(server-1, 20), (server-2, 5), (server-3, 10)] -> Choose server-1 with 20/35 probability.
	"""
	weights = [item[1] for item in servers]
	total = sum(weights) 
	test = random.randint(1, total)
	for item in servers:
		if item[1] >= test:
			return item[0]
		test -= item[1]

if __name__ == "__main__":

	print "Testing anagrams"
	print anagrams(["cab", "bac", "dab", "bad", "bdc"])

	print "Testing matching parens"
	print "Should be True: %s" % (match_p(["(", "{", "(", ")", "}", ")"]))
	print "Should be False: %s" % (match_p(["(", "{", "(", "}", ")"]))
	print "Should be True: %s" % (match_p(["(", "{", "}", ")"]))
	print "Should be False: %s" % (match_p(["(", "{", "(", "}", "}", ")"]))
	print "\n \n" 

	print "Testing encode"
	print "3bq: %s" % (deenc("3bq"))
	print "\n \n" 


	servers = []
	for i in range(5):
		build = 'server-' + str(i)
		servers.append((build, random.randint(0, 30)))
	print servers
	print "\n \n"


	print "Running speed test"
	t0 = time()
	weighted_prob(servers)
	t1 = time()
	print 'weighted_prob takes %f seconds' % (t1-t0)
	print "\n \n"


	print "Running accuracy test"
	seen = {}
	for i in range(25):
		w = weighted_prob(servers)
		if w in seen:
			seen[w] += 1
		else:
			seen[w] = 1
	print seen

