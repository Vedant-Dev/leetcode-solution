def isPalindrome(x: int) -> bool:
	if x.bit_length() > 32:
		return False
	result = 0
	copy = x
	if x < 0:
		return False
	while(x != 0):
		result = (result * 10) + (x % 10)
		x = x // 10
	return (copy == result)