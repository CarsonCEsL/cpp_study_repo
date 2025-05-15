from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        p = 0
        q = 1
        tmp = 0
        while q < len(nums):
            if nums[q] != 0 and nums[p] == 0:
                tmp = nums[p]
                nums[p] = nums[q]
                nums[q] = tmp
                p = p + 1
                q = q + 1
            elif nums[p] == 0:
                p = p + 1
            else:
                p = p + 1
                q = q + 1
        

        return nums
    
    def moveZeroes2(self, nums: List[int]) -> None:
        left = 0
        for right in range(len(nums)):
            if nums[right] != 0:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
        
        return nums


def main():
    print(Solution().moveZeroes2([1, 0, 1]))

main()

