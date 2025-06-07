def longest_common_prefix(strings:list[str]) -> str:
    letter_map = {}
    prefix = ""
    for string in strings:
        counter = 0
        if string[counter] not in letter_map:
            letter_map[string[counter]] = 1
            counter +=1
        else:
            letter_map[string[counter]] +=1
            counter +=1
        
        if letter_map.get(string[counter]) is not None and letter_map[string[counter]] == len(strings):
            prefix += string[counter]
    return prefix
    

if __name__ == "__main__":
    print(longest_common_prefix(["flower","flow","flight"]))