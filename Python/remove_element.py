class Solution:
	def removeElement(self, nums: List[int], val: int) -> int:
		pointer = -1
		nums.sort()
		for index,num in enumerate(nums):
			if num == val and pointer == -1:
				pointer = index
			if num != val and pointer != -1:
				nums[pointer], nums[index] = nums[index],nums[pointer]
				pointer += 1
		return pointer if pointer >= 0 else len(nums)