class Solution:
     
     def Bubble_Sort(self, arr):
          # Find the length
          n = len(arr)
          # run the outer for loop  n-1 times
          for i in range(n - 1):
               flag = 0
               # run the inner for loop n-i-1 times
               for j in range(n - i - 1):
                    # if the element at index j is greater than the element at index j+1, swap
                    if arr[j] > arr[j + 1]:
                         arr[j], arr[j + 1] = arr[j + 1], arr[j]
                         flag = 1
               if flag == 0:
                    break
                         
     def Print_arr(self, arr):
          for i in arr:
               print(i, end = ' ')
          print()
          
# initialize array
arr = [5,  3, 8, 4, 2]
# create an instance of the class
sol =  Solution()
# call the function to sort the array
# call the function to print the array
print("Original array")
sol.Print_arr(arr)
print("Sorted array")
sol.Bubble_Sort(arr)
sol.Print_arr(arr)



