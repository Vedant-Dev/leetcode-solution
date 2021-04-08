class Solution:
	def search(self, nums: List[int], target: int) -> int:
		lb = 0
		ub = len(nums) - 1
		while lb <= ub:
			if nums[lb] == target:
				return lb
			if nums[ub] == target:
				return ub
			lb += 1
			ub -= 1
		return -1