from typing import List
def topKFrequent(nums: List[int], k: int) -> List[int]:
    count = {}
    final = []
    bucket = []
    bucket_size = len(nums) + 1

    for n in nums:
        count[n] = count.get(n, 0) + 1

    for _ in range(bucket_size):
        bucket.append([])


    for c in count:
        bucket[count[c]].append(c)

    b = bucket_size - 1
    while b >= 0:
        print("b: ",b)
        for n in bucket[b]: 
            final.append(n)
        if len(final) == k:
            break
        b -= 1

    print("final: ", final)

    return final


if __name__ == "__main__":
    topKFrequent([1,2,2,3,3,3], 2)
    topKFrequent([7,7],1)
    topKFrequent([1,2],2)