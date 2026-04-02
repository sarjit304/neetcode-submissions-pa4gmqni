class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1

        while i < j:
            while not self.isAlphaNum(s[i]) and i < len(s) - 1:
                i += 1
            while not self.isAlphaNum(s[j]) and j > 0:
                j -= 1     
            if i > j:    
                break       
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
            
        return True        

    def isAlphaNum(self, char):
        ascii_val = ord(char)
        # nums 0-9
        if ascii_val >= 48 and ascii_val <= 57:
            return True
        # chars A-Z
        elif ascii_val >= 65 and ascii_val <= 90:
            return True
        # chars a-z
        elif ascii_val >= 97 and ascii_val <= 122:
            return True
        else:
            return False