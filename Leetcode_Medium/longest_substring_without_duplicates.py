def length_of_longest_substring(s: str) -> int:
    l = 0
    length = 0
    char_set = set()

    for r in range(len(s)):
        while s[r] in char_set:
            char_set.remove(s[l])
            l += 1

        char_set.add(s[r])
        w = (r - l) + 1
        length = max(length, w)
        
    return length


if __name__ == "__main__":
    output = length_of_longest_substring("zxyzxyz")
    print(output)