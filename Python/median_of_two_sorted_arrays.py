class Solution:
	def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
		if nums1 and nums2:
			if not nums1[-1] < nums2[0]:
				list = sorted(nums1 + nums2)
			else:
				 list = nums1 + nums2
		else:
			list = nums1 + nums2
		n = len(list)
		if n % 2 == 0:
			return ((list[int(n/2) - 1] + list[int((n + 2)/2) - 1]) / 2) * 1.0
		else:
			return (list[int((n+1)/2) - 1]) * 1.0
		