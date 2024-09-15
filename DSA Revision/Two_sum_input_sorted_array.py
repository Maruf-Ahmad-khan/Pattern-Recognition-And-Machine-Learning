# # Two Sum II - Input Array Is Sorted
# Example 1:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

class Solution:
     from typing import List
     def twoSum(self, numbers: List[int], target: int) -> List[int]:
          low , high = 0, len(numbers) - 1
          while low <= high:
               if numbers[low] + numbers[high] == target:
                    return  [low + 1, high + 1]
               elif numbers[low] + numbers[high] < target:
                    low += 1
               else:
                    high -= 1
          return []
     
numbers = [2,7,11,15]
target =  9

sol = Solution()
print("Your target would be : ")
print(sol.twoSum(numbers,target))

          