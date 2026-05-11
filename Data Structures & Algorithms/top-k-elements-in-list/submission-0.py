class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
            freq[count[num]].append(num)
            if count[num] > 1:            
                freq[count[num]-1].remove(num)

        result = []
        i = len(freq) - 1
        while i > 0:
            for num in freq[i]:
                result.append(num)
                if len(result) == k:
                    return result
            i -= 1
        return result

            