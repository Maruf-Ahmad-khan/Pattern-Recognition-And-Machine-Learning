# Rotate Array
# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

class Solution:
     from typing  import List

     def rotate(self, nums: List[int], k: int) -> None:
          """Do not return anything, modify nums in-place instead.
          """  
          # Find the lenght of the list
          n = len(nums)
          # create an empty list  to store the rotated array
          rotated = [0] * n
          # Iterate the list
          for i in range(n):
               # calculate the new index
               rotated[(i +  k) % n] = nums[i]
               # copy the rotated list to the original list
          nums[:] = rotated[:]
          
nums = [1,2,3,4,5,6,7]
k = 3
sol = Solution()
sol.rotate(nums, k)
print("The rotated  array is: ", nums)

