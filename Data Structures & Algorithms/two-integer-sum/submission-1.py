class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_sum = {}
        for i in range(len(nums)):
            if(nums[i] in dict_sum):
                return [dict_sum[nums[i]], i]
            else:
                dict_sum[target - nums[i]] = i
        return [0, 0]