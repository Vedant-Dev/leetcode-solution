def find(nums):
	prev_hash = {}
	le = 0
	for index,num in enumerate(nums):
		if num not in prev_hash:
			nums[le], nums[index] = nums[index],nums[le]
			prev_hash[num] = index
			le += 1
	return le
		

print(find([1,1,2])) # 2, [1,2]
print(find([0,0,1,1,1,2,2,3,3,4])) # 5, [0,1,2,3,4]