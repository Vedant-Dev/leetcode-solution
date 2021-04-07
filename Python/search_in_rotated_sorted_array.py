import time

def find(nums,target):
	lb = 0
	lb_2 = 1
	ub = len(nums) - 1
	ub_2 = len(nums) - 2

	while lb <= ub:
		if nums[lb] == target:
			return lb
		if nums[ub] == target:
			return ub
		if nums[lb_2] == target:
			return lb_2
		if nums[ub_2] == target:
			return ub_2
		lb += 1
		ub -= 1
		lb_2 += 1
		ub_2 -= 1
	return -1
print(find([3,2,5,4,1,2,57,8,9,6,2,4,4], 3))