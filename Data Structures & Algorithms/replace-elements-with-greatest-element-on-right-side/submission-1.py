class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n=len(arr)
        rightMax=-1
        newMax=-1
        for i in range (n-1,-1,-1):
            newMax=max(rightMax,arr[i])
            arr[i]=rightMax
            rightMax=newMax

        return arr