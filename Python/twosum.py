
def twoSum(nums: List[int], target: int) -> List[int]:
	flag = 0
	for x,item1 in enumerate(nums):
		for y,item2 in enumerate(nums):
			if item1 + item2 == target and x != y :
				return [x,y]
		return []