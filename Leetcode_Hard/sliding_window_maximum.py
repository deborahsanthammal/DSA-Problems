from collections import deque
from typing import List

def maxSlidingWindow(nums: List[int], k: int) -> int:
    dq = deque()
    output = []
    l = 0
    for r in range(len(nums)):
        if dq and dq[0] <= (r - k):
            dq.popleft()

        while dq and nums[dq[-1]] < nums[r]:
            dq.pop()

        dq.append(r)

        if r >= k-1:
            output.append(nums[dq[0]])
            l += 1

    return output



if __name__ == "__main__":
    output = maxSlidingWindow([1,2,1,0,4,2,6], 3)
    print(output)