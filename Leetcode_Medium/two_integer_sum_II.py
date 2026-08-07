from typing import List

def twoSum(numbers: List[int], target: int) -> List[int]: 
    left_pointer = 0
    right_pointer = len(numbers) - 1
    while left_pointer <= right_pointer:
        if numbers[left_pointer] + numbers[right_pointer] == target:
            return [left_pointer, right_pointer]
        elif numbers[left_pointer] + numbers[right_pointer] > target:
            right_pointer -= 1
        else:
            left_pointer += 1


if __name__ == "__main__":
    output = twoSum([1,2,3,4], 3)
    print(output)