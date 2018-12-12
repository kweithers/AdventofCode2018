serial_id = 2694

import numpy as np
from scipy.ndimage.filters import uniform_filter

nums = np.zeros((300, 300))

for y in range(1, 301):
    for x in range(1, 301):
        rack = x + 10
        powerlevel = rack * y
        powerlevel += serial_id
        powerlevel *= rack
        powerlevel //= 100
        powerlevel %= 10
        nums[y-1][x-1] = powerlevel - 5


def largest_sum_index(a, n):
    idx = uniform_filter(a.astype(float),size=n, mode='constant',cval=-999).argmax()
    return np.unravel_index(idx, a.shape)

# Part 1
y, x = largest_sum_index(nums, 3)
print(x, y)

# Part 2
totals_by_size = {}

for i in range(301):
    y, x = largest_sum_index(nums, i)
    # largest_sum_index returns the center, we want the top-left region
    y1 = y - i // 2
    x1 = x - i // 2
    total = nums[y1:y1+i,x1:x1+i].sum()
    totals_by_size[x1, y1, i] = total

x, y, size = max(totals_by_size, key=totals_by_size.__getitem__)
print(x+1, y+1, size)