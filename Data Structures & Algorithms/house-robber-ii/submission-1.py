class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        if n==0:
            return 0
        if n==1:
            return nums[0]
        def robLine(arr):
            m=len(arr)

            if m==1:
                return arr[0]
        
            prev2=arr[0]
            prev1=max(arr[0],arr[1])

            for i in range(2,m):
                current=max(prev1, arr[i]+prev2)
                prev2=prev1
                prev1=current
            return prev1
            
        case1=robLine(nums[:-1])
        case2=robLine(nums[1:])
        return max(case1,case2)
        