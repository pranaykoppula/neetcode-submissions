class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        m, ctr, i, n = 0, 0, 0, len(nums)
        while i<n:
            while i<n and nums[i]==1:
                ctr+=1
                i+=1
            m=max(m,ctr)
            ctr=0
            i+=1
        return m

        