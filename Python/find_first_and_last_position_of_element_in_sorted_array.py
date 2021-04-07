def find(nums,target):
	lb,ub = -1,-1
	for index, num in enumerate(nums):
		if lb == -1 and num == target:
			lb = index
		if ub == -1 and num == target and lb != -1:
			if index == len(nums) - 1:
				ub = index
				break
			if nums[index + 1] != target:
				ub = index
				break
	return [lb,ub]

print(find([5,7,7,8,8,10],8))
