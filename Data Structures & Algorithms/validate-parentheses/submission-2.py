class Solution:
    def isValid(self, s: str) -> bool:
        braces_pair = {
            '(': ')',
            '{':'}', 
            '[':']'
        }
        tracker = []
        for bracket in s:
            if bracket in braces_pair.keys():
                tracker.append(bracket)
            else:
                if len(tracker) > 0:
                    last_opening_bracket = tracker.pop()
                    if bracket != braces_pair[last_opening_bracket]:
                        return False
                else:
                    return False
        if len(tracker) > 0:
            return False
        return True