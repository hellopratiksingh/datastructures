class Solution(object):
    def isPalindrome(self, s):
        i, j = 0, len(s)-1
        while i <= j:
            while i < j and not self.alphanum(s[i]):
                i += 1
            while j > i and not self.alphanum(s[j]):
                j -= 1

            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1
        return True

    def alphanum(self, c):
        return (65 <= ord(c) <= 90) or (97 <= ord(c) <= 122) or (48 <= ord(c) <= 57)
