class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        data = defaultdict(list)

        for word in strs:
            sorted_key = "".join(sorted(word))
            data[sorted_key].append(word)

        return list((data.values()))