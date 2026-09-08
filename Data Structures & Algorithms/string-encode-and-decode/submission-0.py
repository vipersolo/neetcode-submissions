class Solution:

    def encode(self, strs: List[str]) -> str:
        # 5#hello5#world
        encoded_string=""
        for word in strs:
            encoded_string=encoded_string+str(len(word))+"#"+word
        return encoded_string

    def decode(self, s: str) -> List[str]:
        i=0
        decoded_string=[]
        while i < len(s):
            delimiter = s.index("#",i)
            length = int(s[i:delimiter])
            j = delimiter + 1
            decoded_string.append(s[j : j + length])
            i=j+length
        return decoded_string


