class Solution:
	def isPalindrome(self, x: int) -> bool:
		if x < 0:
			return False
		rev = int("".join(reversed(str(x))))
		return (x == rev)