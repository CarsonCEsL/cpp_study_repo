from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        for i in range(len(digits) - 1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                return digits
            else:
                digits[i] = 0
        
        return [1] + digits

def main():
    solution = Solution()
    print(solution.plusOne([1, 2, 3]))
    print(solution.plusOne([1, 9]))
    print(solution.plusOne([9, 9, 9]))

main()