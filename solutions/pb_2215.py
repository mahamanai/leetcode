def findDifference(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    set1 = set(nums1)
    set2 = set(nums2)
    return [list(set1 - set2), list(set2 - set1)]

def findDifference2(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    answer1 = filter(lambda i:i not in nums2, nums1)
    answer2 = filter(lambda i:i not in nums1, nums2)

    return [list(set(answer1)), list(set(answer2))]

def findDifference3(nums1: list[int], nums2: list[int]) -> list[list[int]]:
    set1, set2 = set(nums1), set(nums2)
    res1, res2 = set(), set()
    
    for s in set1:
        if not s in set2:
            res1.add(s)
    
    for s in set2:
        if not s in set1:
            res2.add(s)

    return [list(res1), list(res2)]