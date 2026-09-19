
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counts = defaultdict(int)

        if len(s) != len(t):
            return False

        for char in s:
            counts[char] += 1
        
        for char in t:
            counts[char] -= 1

            if counts[char] < 0:
                return False
        return True
        return True        