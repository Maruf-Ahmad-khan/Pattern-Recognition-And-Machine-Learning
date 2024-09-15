# Remove Duplicates from Sorted Array
class Solution:
     from typing import List
     def removeDuplicates(self, nums: List[int]) -> int:
          count = 1
          for i in range(1,len(nums)):
               if nums[i - 1] != nums[i]:
                    nums[count] = nums[i]
                    count += 1
          return count
     
nums = [1,1,2,2,3,4,4]
sol = Solution()
unique_count = sol.removeDuplicates(nums)
# Print the result
print("List after removing duplicates:", nums[:unique_count])
print("Number of unique elements:", unique_count)         