def is_anagram(s: str, t: str) -> bool:
    s_dict = {}
    for i in s:
        s_dict[i] = 1 + s_dict.get(i, 0)

    t_dict = {}
    for i in t:
        t_dict[i] = 1 + t_dict.get(i, 0)

    if s_dict == t_dict:
        return True
    else:
        return False

def is_anagram2(s: str, t: str) -> bool:
    return sorted(s) == sorted(t)

def is_anagram3(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False

    count_s = {}
    for i in s:
        count_s[i] = 1 + count_s.get(i, 0)

    for i in t:
        count_s[i] = count_s.get(i, 0) - 1  

    for i in count_s.values():
        if i != 0:
            return False
        
    return True