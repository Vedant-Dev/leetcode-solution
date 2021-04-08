class Solution:
	def firstMissingPositive(self, nums) -> int:
		result = 1
		nums.sort()
		for num in nums:
			if num > 0:
				if num == result:
					result += 1
				elif num > result:
					return result
		return result

s = Solution()
print(s.firstMissingPositive([7,8,9,11,12]))