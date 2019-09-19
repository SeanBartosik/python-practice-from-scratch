# Task: Return a list of the two indexes of the two numbers in a list that
# add up to the target value. i.e. for a target of 4 in nums = [1,3,5,7]
# returns [0,1]. If no combination exists, return None


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}

        for i in range(len(nums)):
            if target-nums[i] not in hash:
                hash[nums[i]] = i
            else:
                return [hash[target-nums[i]], i]


numbers = [2, 7, 11, 15]
test = Solution()
print(test.twoSum(numbers, 9))
