from typing import List

def dailyTemperatures(temperatures: List[int]) -> List[int]:
    stack = []
    output = [0] * len(temperatures) 
    for index, element in enumerate(temperatures):
        while stack and temperatures[stack[-1]] < element:
            top = stack.pop()
            difference = index - top
            output[top] = difference

        stack.append(index)

    return output



if __name__ == "__main__":
    output = dailyTemperatures([30,38,30,36,35,40,28])
    print(output)

        