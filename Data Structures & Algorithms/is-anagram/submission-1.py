class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts={}
        dictst={}
        if len(s) != len(t):
            return False
        for i in s:
            if i not in dicts:
                dicts[i]=1
            else:
                dicts[i]=dicts.get(i,0) + 1
        
        for j in t:
            if j not in dictst:
                dictst[j]=1
            else:
                dictst[j]=dictst.get(j,0) + 1
        
        return dicts == dictst