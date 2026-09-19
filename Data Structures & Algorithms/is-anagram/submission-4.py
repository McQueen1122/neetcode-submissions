class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = sorted(s)
        second = sorted(t)
        if len(first) != len(second):
            return False
        else:
            for i in range(len(first)):
                if first[i] != second[i]:
                    return False
            return True

