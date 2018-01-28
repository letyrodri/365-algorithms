def min_max_sum(arr):
	'''
	Interesting simple and easy hack rank problem

	Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

	Input Format

	A single line of five space-separated integers.

	Constraints

	Each integer is in the inclusive range .
	Output Format

	Print two space-separated long integers denoting the respective minimum and maximum values that can be calculated by summing exactly four of the five integers. (The output can be greater than 32 bit integer.)

	Sample Input

	1 2 3 4 5
	Sample Output

	10 14
	'''
	return sum(arr)-max(arr), sum(arr)-min(arr)