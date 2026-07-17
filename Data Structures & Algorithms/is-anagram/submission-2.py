class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        letters = {}
        count_s = 0
        count_t = 0
        for char in s:
            count_s += 1
            if char not in letters:
                letters[char] = 1
            else:
                letters[char] += 1
        for char in t:
            count_t += 1
            if char not in letters or letters[char]==0:
                return False
            letters[char] -= 1
       
        return True