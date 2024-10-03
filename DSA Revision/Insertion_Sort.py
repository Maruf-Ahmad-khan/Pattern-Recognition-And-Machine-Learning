class Solution:
     def Insertion_Sort(self, arr):
          n = len(arr)
          for i in range(1, n):
               temp = arr[i]
               j = i - 1
               while j >= 0 and arr[j] > temp:
                    arr[j + 1] = arr[j]
                    j -= 1
               arr[j + 1] = temp
               
     def Print_Arr(self, arr):
          for i in arr:
               print(i, end = ' ')
          print()

arr = [7, 3, 5, 1]
sol = Solution()
print("Original Array")
sol.Print_Arr(arr)
print("Sorted Array")
sol.Insertion_Sort(arr)
sol.Print_Arr(arr)