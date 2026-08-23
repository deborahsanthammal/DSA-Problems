from typing import List

def carFleet(target: int, position: List[int], speed: List[int]) -> int:
    pair = []
    stack = []
    for p, s in zip(position, speed):
        pair.append([p,s])

    reverse_order = sorted(pair, reverse=True)

    for p, s in reverse_order:
        distance = (target - p) / s
        stack.append(distance)

        if len(stack) >= 2 and stack[-1] <= stack[-2]:
            stack.pop()
    return len(stack)



if __name__ == "__main__":
    output = carFleet(10, [4,1,0,7], [2,2,1,1])
    print(output)