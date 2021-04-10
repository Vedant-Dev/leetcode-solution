#taken from discussion tab of leetcode
class Solution(object):
	def trap(self, height):
		if not height or len(height) < 3:
			return 0
		
		n = len(height)
		l_max = [None] * n
		l_max[0] = height[0]
		r_max = [None] * n
		r_max[n-1] = height[n-1]
		i = 1 
		j = n-2
		
		while i < n and j >= 0:
			l_max[i] = max(l_max[i-1],height[i])
			r_max[j] = max(r_max[j+1], height[j])
			i+=1
			j-=1

		total_sum = 0
		for i in range(1, n-1):
			total_sum += min(r_max[i], l_max[i]) - height[i]
		
		return total_sum
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