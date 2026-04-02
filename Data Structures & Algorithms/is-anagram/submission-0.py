class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map = {}
        for char in s:
            if map.get(char) is not None:
                map[char] += 1
            else:
                map[char] = 1
        for char in t:
            if map.get(char) is not None:
                if map[char] > 0:
                    map[char] -= 1
                else:
                    return False
            else:
                return False
        return True