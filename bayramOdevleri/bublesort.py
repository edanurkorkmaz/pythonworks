def sort(nums):
  
  for i in range(0,len(nums)):
      for j in range(0,len(nums)-1):
          if nums[j] > nums[j+1] :
              nums[j],nums[j+1]=nums[j+1],nums[j]
          else:
              continue
  print(nums)
  
List=[90,50,64,72]
sort(List)