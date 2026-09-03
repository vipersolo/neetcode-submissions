class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict={}
        for i in nums:
            dict[i]=dict.get(i,0) + 1
        result = sorted(dict,key=dict.get,reverse = True)[:k]
        return result

