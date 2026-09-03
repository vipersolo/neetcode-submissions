class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq={}
        for num in nums:
            freq[num]=freq.get(num,0)+1
        arr=[[]for _ in range(len(nums)+1)]

        for key,value in freq.items():
            arr[value].append(key)
        
        result = []
        for i in range(len(arr)-1,-1,-1):
            for j in arr[i]:
                result.append(j)
                if len(result) == k:
                    return result
        return result

