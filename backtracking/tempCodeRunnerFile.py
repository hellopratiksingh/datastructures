h2 = int(current[:2])
	m2 = int(current[3:])
	
	h1 = int(correct[:2])
	m1 = int(correct[3:])
 
	if (h1 == h2):
		diff = m2-m1
	else:
		diff = abs(((h2-h1-1)*60 + (60-m1) + m2))	
	
	res = 0
	if diff >= 60:
		z = diff // 60
		diff = diff % 60
		res += z
	if diff >= 15:
		z = diff // 15
		diff = diff % 15
		res += z
	if diff >=5:
		z = diff // 5
		diff = diff % 5
		res += z
	if diff >=1:
		z = diff // 1
		diff = diff % 1
		res += z
	return res