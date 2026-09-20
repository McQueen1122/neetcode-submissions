class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""

        for word in strs:
            s += str(len(word)) + "#" + word

        return s

    def decode(self, s: str) -> List[str]:
        strs = []
        index = 0

        while index < len(s):

            # Find '#'
            j = index
            while s[j] != "#":
                j += 1

            length = int(s[index:j])

            start = j + 1
            end = start + length

            strs.append(s[start:end])

            index = end

        return strs