class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return bool(Counter(s) == Counter(t))


