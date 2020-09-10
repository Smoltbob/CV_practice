def longinc(nums):
        """
        Naive : for each element, count while it increases
        """
        if not nums:
            return 0
        
        if len(nums) == 1:
            return 1
        
        dp = [1] * len(nums)

        for i in range(len(nums), -1, -1):
            for j in range(i, len(nums)):
                if nums[j] > nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
      
        return max(dp)
