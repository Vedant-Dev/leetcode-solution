# def find(height):
# 	max_area = 0
# 	x = 0
# 	y = 0
# 	n = len(height)
# 	for x in range(0,n):
# 		for y in range(x,n):
# 			temp_area = 0
# 			h = min(height[x],height[y])
# 			b = abs(x - y)
# 			temp_area = h * b
# 			if temp_area > max_area:
# 				max_area = temp_area
# 	return max_area

def find(height):
	l = 0
	r = len(height) -1
	area = 0 
	while l < r:
        # Calculating the max area
		area = max(area, min(height[l],height[r]) * (r - l))
		if height[l] < height[r]:
			l += 1
		else:
			r -= 1
	return area
		#
print(find([1,8,6,2,5,4,8,3,7]))
print(find([1,1]))
print(find([4,3,2,1,4]))
print(find([1,2,1]))