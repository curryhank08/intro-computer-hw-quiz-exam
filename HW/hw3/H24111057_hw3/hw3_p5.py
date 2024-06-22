"""
author: H24111057 統計系 姚博瀚
"""

def max_trapped_water(heights):
    n = len(heights)
    left_max = [0] * n
    right_max = [0] * n
    water = [0] * n
    
    # Calculate the maximum height to the left of each index
    i = 0
    left_max[i] = heights[i]
    i += 1
    while i < n:
        left_max[i] = max(left_max[i-1], heights[i])
        i += 1
    
    # Calculate the maximum height to the right of each index
    i = n-1
    right_max[i] = heights[i]
    i -= 1
    while i >= 0:
        right_max[i] = max(right_max[i+1], heights[i])
        i -= 1
    
    # Calculate the amount of water that can be trapped at each index
    i = 0
    while i < n:
        water[i] = min(left_max[i], right_max[i]) - heights[i]
        i += 1
    
    # Calculate the total amount of water that can be trapped
    total_water = 0
    i = 0
    while i < n:
        total_water += water[i]
        i += 1
    
    return total_water
    
# example usage
heights = input("Input sequence of seats: ")
heights = [int(h) for h in heights.split()]
max_water = max_trapped_water(heights)
print(f"water: {max_water}")
