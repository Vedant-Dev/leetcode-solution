class Solution:
	def combinationSum(self, candidates, target):
		prev_hash = {}
		result = []
		for index, num in enumerate(candidates):
			prev_hash[num] = index

		for num in candidates:
			pair = target - num
			print(pair)
			if pair == 0:
				result.append([num])
			if pair in prev_hash:
				result.append([num, pair])
		return result

s = Solution()
print(s.combinationSum([2,3,6,7],7))