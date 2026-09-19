class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mpp={}
        for i in range(len(nums)):
            num=nums[i]
            more=target-num
            if more in mpp:
                return [mpp[more],i]
            mpp[num]=i
        return [-1,-1]