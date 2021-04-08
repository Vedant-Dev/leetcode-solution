class Solution:
	def searchInsert(self, nums, target) -> int:
		lb = 0
		ub = len(nums) - 1

		while lb <= ub:
			mid = int((lb + ub) // 2)
			if nums[ub] < target:
				return ub + 1
			if nums[lb] > target:
				if lb == 0:
					return 0
				return lb
			if nums[mid] == target:
				return mid
			elif nums[mid] > target:
				ub = mid - 1
			elif nums[mid] < target:
				lb = mid + 1
		return -1

sl = Solution()
print(sl.searchInsert([1,3,5,6],5)) #2
print(sl.searchInsert([1,3,5,6],2)) #1
print(sl.searchInsert([1,3,5,6],7)) #4
print(sl.searchInsert([1,2,9,11],8)) #0
print(sl.searchInsert([1],0)) #0