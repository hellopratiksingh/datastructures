
def check_anagram(str1, str2):
    count = [0] * 256
    if len(str1) != len(str2):
        return False

    for i in range(0, len(str1)):
        ascii_ = ord(str1[i])
        count[ascii_] += 1

    for i in range(0, len(str2)):
        ascii_ = ord(str2[i])
        count[ascii_] -= 1

    for i in range(0, 256):
        if count[i] != 0:
            return False
    return True


print(check_anagram(str1='aabcd', str2='abbcd'))
