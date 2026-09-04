class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c1={}
        for i,n in enumerate(nums):
            diff=target-n
            if diff in c1:
                return [c1[diff],i]
            c1[n]=i