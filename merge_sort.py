def merge_sort(a):
	if len(a) == 1:
		return a

	middle = len(a) // 2

	b = merge_sort(a[:middle])
	c = merge_sort(a[middle:])

	return merge(b,c)

def merge(b,c):
	idx_b = 0 # Index for b array (arrow)
	idx_c = 0 # Index for c array (arrow)

	res = []

	# Iterate while the end of any array is reached
	while(idx_b < len(b) and idx_c < len(c)):
		
		if b[idx_b] <= c[idx_c]:
			res.append(b[idx_b])
			idx_b += 1

		else:
			res.append(c[idx_c])
			idx_c += 1


	# Appends the remains of the b array
	while(idx_b < len(b)):
		res.append(b[idx_b])
		idx_b += 1

	# Appends the remains of the c array
	while(idx_c < len(c)):
		res.append(c[idx_c])
		idx_c += 1

	return res		


