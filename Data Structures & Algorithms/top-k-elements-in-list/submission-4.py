
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count frequencies
        freq = Counter(nums)

        # Step 2: Sort items by frequency (descending)
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        # Step 3: Extract the top k elements
        result = [item[0] for item in sorted_items[:k]]
        return result



        
