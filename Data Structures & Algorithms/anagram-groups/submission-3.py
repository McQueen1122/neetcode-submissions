class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = defaultdict(list)
        
        for word in strs:
            # Create a count array for the 26 lowercase English letters
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            
            # Tuples are immutable and can be used as dictionary keys
            data[tuple(count)].append(word)
            
        return list(data.values())
