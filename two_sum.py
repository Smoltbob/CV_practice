def binary_search(array, target):
    lower = 0
    upper = len(array)
    while lower < upper:   # use < instead of <=
        x = lower + (upper - lower) // 2
        val = array[x]
        if target == val:
            return x
        elif target > val:
            if lower == x:   # these two are the actual lines
                break        # you're looking for
            lower = x
        elif target < val:
            upper = x

class Solution:        
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums = [(x, i) for i, x in enumerate(nums)] # save original indices before sorting
        nums = sorted(nums, key=lambda x: x[0])
        tmp = [x[0] for x in nums]
        for cpt,n in enumerate(tmp):
            res = binary_search(tmp[cpt+1:], target-n) # search for the complement
            if res is not None:
                res += cpt +1
                return [nums[cpt][1], nums[res][1]]
        
        
   
