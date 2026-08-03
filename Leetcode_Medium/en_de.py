from typing import List

def encode(strs: List[str]) -> str:
        output = ""

        for s in strs:
             output += str(len(s)) + ":" + s

        return output


def decode(s: str) -> List[str]:
    length = ""
    output = []
    i = 0
    while i < len(s):
          if s[i] != ":":
                length += s[i]
                i += 1
          else:
                word_length = int(length)
                length = ""
                word = s[i+1: i+word_length+1]
                output.append(word)
                i = i + word_length + 1

    return output


if __name__ == "__main__":
    #  input = ["My", "name", ":issssssss", "Deborah"]
     input = ["",""]
     encoded = encode(input)
     print("encoded: ", encoded)
     decoded = decode(encoded)
     print("decoded: ", decoded)
