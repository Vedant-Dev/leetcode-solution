class Solution:
	def twoSum(self, nums: List[int], target: int) -> List[int]:
		flag = 0
		storage = {}
		for row,item in enumerate(nums):
			pair_num = target - item
			if pair_num in storage:
				return [row,storage[pair_num]]
			storage[item] = row
		return []