class Solution:
    def encode(self, strings):
        encoded = ""
        for s in strings:
            n = str(len(s))
            encoded += n + "#" + s
        
        return encoded

##      4#neet4#code4#love3#you
        
    def decode(self, encoded):
        strings = []
        i = 0
        while i < len(encoded):
            j = i
            while encoded[j] != '#':
                j += 1
            length = int(encoded[i:j])
            strings.append(encoded[j+1:j+1+length])
            i = j + length + 1
        return strings


        