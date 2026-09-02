class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        dict={}
        for word in strs:
            count=[0]*26
            for char in word:
                count[ord(char)-ord('a')]+=1
            signature=tuple(count)

            if signature not in dict:
                dict[signature]=[]
            dict[signature].append(word)

        return list(dict.values())
