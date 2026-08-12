from typing import List

def maxArea(heights: List[int]):
    l, r = 0, len(heights) - 1
    res = 0 
    while l < r:
        width = r - l
        height = min(heights[l], heights[r])
        area = width * height
        res = max(res, area)
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1

    return res


if __name__ == "__main__":
    output = maxArea([2,2,2])
    print(output)

