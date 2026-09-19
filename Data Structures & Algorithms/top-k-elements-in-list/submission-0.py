class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        answer = []
        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)

        print(sorted_items)
        for key in sorted_items:
            if k > 0:
                answer.append(key[0])
                k -= 1
    
        print(answer)
        return answer   
        