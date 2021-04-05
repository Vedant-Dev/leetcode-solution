def median(l1,l2):
	if not l1[-1] < l2[0]:
		l = sorted(l1 + l2)
	else:
		l = l1 + l2
	n = len(l)
	sum = 0
	if n % 2 == 0:
		sum = (l[int(n/2) - 1] + l[int((n + 2)/2) - 1]) / 2
	else:
		sum = l[int((n+1)/2) - 1]
	return sum * 1.0