class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts={}
        dictst={}
        if len(s) != len(t):
            return False
        for i in s:
                dicts[i]=dicts.get(i,0) + 1
                  
        for j in t:
                dictst[j]=dictst.get(j,0) + 1
        
        return dicts == dictst