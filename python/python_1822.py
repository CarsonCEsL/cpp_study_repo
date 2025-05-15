from typing import List


class Solution:

    def signFunc(self, num: int) -> int:
        if (num > 0):
            return 1
        elif (num == 0):
            return 0
        else:
            return -1

    def arraySign(self, nums: List[int]) -> int:
        
        result = 1

        for e in nums:
            result *= e
        

        return self.signFunc(result)
    
    def arraySign2(self, nums: List[int]) -> int:

        result = 1

        for e in nums:
            if (e == 0):
                return 0
            elif (e < 0):
                result *= -1
        
        return result

def main():
    solution = Solution()
    print(solution.arraySign([1,2,0,4,7]))

main()