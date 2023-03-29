def removeElement(nums, val) -> int:        
        for pos,elem in enumerate(nums):
            if elem is val:
                nums[pos] = 999999999
        
        nums.sort()
        
        for pos,elem in enumerate(nums):
            if elem  == 999999999 :
                return nums[0:pos]

def remove_element(nums, val):
    k = 0  # initialize the count of elements not equal to val
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]  # move the element to the front
            k += 1  # increment the count
    return k

print(removeElement([2,3,2,3,1,4,2,2,4,5,2],5)) ;#

nums = [2,3,2,3]
print(nums[0:remove_element(nums,2)])