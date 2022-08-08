def isPalindrome(s):
        str_ = ''
        if len(s) == 0:
            return True
        else:
            for i in s:
                if (i>="a" and i<="z" or i>="A" and i<="z" or i>=0 and i<=9):
                    str_ += s[i]
        str_ = str_.lower()
        s = str_
        s = s[::-1]
        
        if str_ == s:
            return True
        else:
            return False
        

print(isPalindrome(s="A man, a plan, a canal: Panama"))
