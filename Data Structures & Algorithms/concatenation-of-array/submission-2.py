class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        i=0
        n=len(nums)
        ans=[0]*2*n
        while i<n*2:
            if i<n:
                ans[i]=nums[i]
            else:
                ans[i]=nums[i-n]
            i+=1
        return ans