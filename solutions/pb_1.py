def twoSum(nums: list[int], target: int) -> list[int]:
    result = set()
    for i in range(len(nums)):
        remainder = target - nums[i] 
        if remainder in (nums[:i] + nums[i+1:]):
            result.add(i)
        if len(result) == 2:
            return list(result)
            
def twoSum2(nums: list[int], target: int) -> list[int]:
    hashmap = {}
    for i, n in enumerate(nums):
        remainder = target - n
        if remainder in hashmap:
            return [hashmap[remainder], i]
        hashmap[n] = i