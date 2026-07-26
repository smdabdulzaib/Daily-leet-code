class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums.sort()
        n1=nums[-1]*nums[-2]*nums[-3]
        n2=nums[0]*nums[1]*nums[-1]
        if n1>n2:
            return n1
        else:
            return n2
