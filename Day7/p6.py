#  Sort a list in ascending and descending order with out using sort?  

nums=[1,3,2,5,8,4,9,4]

for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if nums[i]<nums[j]:
            nums[i],nums[j]=nums[j],nums[i]
        else:
            nums[i],nums[j]=nums[i],nums[j]
            
print(nums)