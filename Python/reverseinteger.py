def reverse(x: int) -> int:
	if x.bit_length() > 32:
		return 0
	negFlag = False
	result = 0
	if x < 0:
		x = -x
		negFlag = True
	while(x != 0):
		result = (result * 10) + (x % 10)
		x = x // 10
	return -result if negFlag else result

print(reverse(-137))