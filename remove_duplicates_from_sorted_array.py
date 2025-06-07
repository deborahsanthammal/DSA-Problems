def get_unique_elements(nums:list):
    unique_elements = {}
    for n in nums:
        if n not in unique_elements:
            unique_elements[n] = 1
        elif n in unique_elements:
            unique_elements[n] += 1

    for n in nums:
        if unique_elements[n] > 1:
            for i in range(unique_elements[n]-1):
                nums.remove(n)

    print("nums ", nums)
    print("unique nums ", unique_elements)

    return len(unique_elements)


def get_unique(nums:list) -> int:
    length = len(nums)
    i = 0
    j = 1
    while j < length:
        if i+1 != length:
            if nums[i] == nums[j]:
                nums.pop(i)
                print("nums ", nums)
            i+=1
            length = len(nums)
    # for n in range(length):
    #     print(n,"nu")
    #     print(length,"length")
    #     print("n+1  ", n+1)
    #     if (n+1) != length:
    #         print("nums ", nums)
    #         if nums[n] == nums[n+1]:
    #             nums.pop(n)
    # print("nums ", nums)
    return len(nums)

if __name__ == "__main__":
    # print(get_unique_elements([1,1,2,2,3,3,3,4,4,5,5,5,5,5]))
    print(get_unique([1,1,2,2,3,3,3,4,4,5,5,5,5,5]))