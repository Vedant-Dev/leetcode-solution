# GfG solution
class Solution:
	def trap(self,height):
		res = 0
		n = len(height)
		for i in range(1, n - 1): 
			left = height[i]
			for j in range(i):
				left = max(left, height[j])
			right = height[i]
			for j in range(i + 1 , n):
				right = max(right, height[j])
			res = res + (min(left, right) - height[i])
		return res
'''

My Solution

class Solution:
	def trap(self, height):
		total_area = 0
		if len(height) == 0:
			return 0
		n = max(height)
		for row in range(1, n + 1):
			area = 0
			lb = -1
			wall = -1
			for index, num in enumerate(height):
				if num >= row:
					wall = index
				if lb == -1:
					if num >= row:
						lb = index
				if lb != -1:
					if num < row:
						area += 1
			area -= (len(height) - wall - 1)
			total_area += area
		return total_area
'''
s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1])) #6
print(s.trap([4,2,0,3,2,5])) #9