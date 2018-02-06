def recursive_fibonacci_sequence(n):
	if n == 1 or n == 2:
		return 1
	else:
		return recursive_fibonacci_sequence(n-2)+recursive_fibonacci_sequence(n-1)
