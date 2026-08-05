from typing import List

def product_of_array(array : List[int]) -> List[int]:

    prefix_array = [0] * len(array)
    postfix_array = [0] * len(array)
    output = []

    i = 1 
    prefix_array[0] = array[0]
    while i < len(array):
        prefix_array[i] = prefix_array[i-1] * array[i]
        i += 1

    i = len(array) - 2
    postfix_array[len(array)-1] = array[len(array)-1]
    while i >= 0:
        postfix_array[i] = postfix_array[i+1] * array[i]
        i -= 1
    i = 0
    while i < len(array):
        prefix = 1 if i == 0 else prefix_array[i-1]
        postfix = 1 if i == len(array) - 1 else postfix_array[i+1]
        output.append(prefix * postfix)
        i += 1


    print(prefix_array)
    print(postfix_array)
    print(output)
    return output

def product_of_array_optimized(array : List[int]) -> List[int]:

    prefix_array = [0] * len(array)
    postfix_array = [0] * len(array)
    output = [0] * len(array)

    i = 1 
    output[0] = 1
    while i < len(array):
        output[i] = output[i-1] * array[i]
        i += 1

    print("output: ", output)

    i = len(array) - 1
    # postfix_array[len(array)-1] = array[len(array)-1]
    while i >= 0:
        if i == len(array) - 1:
            postfix = 1
        else:
            postfix = output[i+1] * array[i]
        output[i] = output[i] * postfix
        i -= 1
    # i = 0
    # while i < len(array):
    #     prefix = 1 if i == 0 else prefix_array[i-1]
    #     postfix = 1 if i == len(array) - 1 else postfix_array[i+1]
    #     output.append(prefix * postfix)
    #     i += 1


    print(prefix_array)
    print(postfix_array)
    print(output)
    return output


if __name__ == "__main__":
    # product_of_array([1,2,4,6])
    product_of_array_optimized([1,2,4,6])