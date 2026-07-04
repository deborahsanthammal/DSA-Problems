from typing import List

def encode(strs: List[str]) -> str:
        output = ""

        for s in strs:
            if strs.index(s) != len(strs) - 1:
                output = output + s + "_" 
            else:
                output += s

        return output


def decode(s: str) -> List[str]:
    print("length: ", len(s))
    for v in s:
         print("ascii: ", ord(v))
    output = s.split("_")

    return output


if __name__ == "__main__":
    #  input = ["My", "name", "is", "Deborah"]
     input = ["",""]
     encoded = encode(input)
     print("encoded: ", encoded)
     decoded = decode(encoded)
     print("decoded: ", decoded)

     print("empty strings: ","" + "")