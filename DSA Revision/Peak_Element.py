class Solution:
     from typing import List
     def  peakIndexInMountainArray(self, arr:List[int])->int:
          # calculate lenght of the array
          n = len(arr)
          # if there is only one element then it is peak
          if(n == 1):
               return  0
          # if first element is greater than the second element then it is peak
          if(arr[0] > arr[1]):
               return 0
          # if second last element is greater than the last element then it is peak
          if (arr[n-1] > arr[n-2]):
               return  n-1
          
          # use of binary search
          low , high = 1, n -2
          while(low <= high):
               mid = (low + high) // 2
               # if mid element is greater than the next element then it is peak
               if(arr[mid -1] < arr[mid] and arr[mid] > arr[mid + 1]):
                    return mid
               elif(arr[mid - 1] < arr[mid]):
                    low = mid + 1
               else:
                    high = mid - 1
                    
          return -1
     
     
arr = [0,1,0]
sol = Solution()
print("The peak element is : ")
print(sol.peakIndexInMountainArray(arr))
                    
               



          