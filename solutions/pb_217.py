def containsDuplicate(nums: list[int]) -> bool:
    set_nums = set(nums)
    if len(set_nums) == len(nums):
        return False
    else:
        return True
        