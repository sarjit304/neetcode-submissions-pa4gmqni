class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        while len(strs):
            current_str = strs.pop(0)
            current_str_anagrams = [current_str]
            pointer = 0
            while pointer < len(strs):
                if self.isAnagram(current_str, strs[pointer]):
                    current_str_anagrams.append(strs.pop(pointer))
                    continue
                pointer += 1

            result.append(current_str_anagrams)
        return result

    def isAnagram(self, str1, str2):
        return sorted(str1) == sorted(str2)