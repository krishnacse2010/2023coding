def removeElement(nums, val) -> int:        
        for pos,elem in enumerate(nums):
            if elem is val:
                nums[pos] = 999999999
        
        nums.sort()
        
        for pos,elem in enumerate(nums):
            if elem  == 999999999 :
                return nums[0:pos]

print(removeElement([2,3,2,3],2))