class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = {}

        # Count characters in string s
        for char in s:
            if char in char_count:
                char_count[char] += 1
            else:
                char_count[char] = 1

        # Decrement counts for string t
        for char in t:
            if char not in char_count or char_count[char] == 0:
                return False
            char_count[char] -= 1

        return True
