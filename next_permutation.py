'''
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such an arrangement is not possible, it must rearrange it as the lowest possible order (i.e., sorted in ascending order).

The replacement must be in place and use only constant extra memory.



Source: https://leetcode.com/problems/next-permutation/
'''

class Solution:
    
        
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        
        i = self.idx_to_change(nums)
        
        if i==-1:
            nums.sort()
            return 
        
        if i == len(nums)-1:
            x = nums[i-1]
            nums[i-1] = nums[i-2]
            nums[i-2] = x
            
        else:
            self.get_next_value(nums,i)
        
    def idx_to_change(self, nums):
        
        j = len(nums)-1
        
        while(j > 0 and nums[j] < nums[j-1]):
            j = j-1
            
        return j-1
        
    def get_next_value(self, nums,i):
        v = nums[i]
        c = nums[i+1]
        at = i+1
        
        # Seach the next value to use
        for j in range(i+2, len(nums)):
            if nums[j] < c and nums[j] > v:
                c = nums[j]
                at = j
                
        # Swamp the values
        nums[i] = c
        nums[at] = v
        
        # Sorts the rest of the array
        for k in range(i+1,len(nums)):
            while(k > i+1 and nums[k] < nums[k-1]):
                nums[k], nums[k-1] = nums[k-1], nums[k]
                k = k-1
        
           
            
                    
            
            
