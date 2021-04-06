def find(nums,val):
	pointer = -1
	nums.sort()
	for index,num in enumerate(nums):
		if num == val and pointer == -1:
			pointer = index
		if num != val and pointer != -1:
			nums[pointer], nums[index] = nums[index],nums[pointer]
			pointer += 1
	print(nums)
	return pointer if pointer >= 0 else len(nums)
		

print(find([2],5)) # 2, nums = [2,2]
print(find([3,3,3,3,3,3,3,3],3)) # 5, nums = [0,1,4,0,3]