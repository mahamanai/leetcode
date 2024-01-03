def is_palindrome(s: str) -> bool:
    i = len(s) - 1
    s1, s2 = '', ''
    for j in range(len(s)):
        if s[i].isalnum():
            s2 += s[i].lower()
        if s[j].isalnum():
            s1 += s[j].lower()
        i -= 1
    return s1 == s2

def is_palindrome2(s: str) -> bool:
    l, r =  0, len(s) - 1
    while l < r:
        while l < r and not s[l].isalnum():
            l += 1
        while r > l and not s[r].isalnum():
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l, r = l + 1, r - 1
    return True