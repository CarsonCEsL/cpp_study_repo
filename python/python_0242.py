class Solution:

    # hash table
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_dict = {}
        t_dict = {}

        if (len(t) != len(s)):
            return False

        for char in s:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1
        
        for char in t:
            if char in t_dict:
                t_dict[char] += 1
            else:
                t_dict[char] = 1
        
        for char in s_dict:
            if s_dict[char] != t_dict.get(char, 0):
                return False
        
        return True
    
    # 异或运算 -- 存在缺陷
    def isAnagram2(self, s: str, t: str) -> bool:

        xor_num = 0
        s_sum = 0
        t_sum = 0
        s_or = 0
        t_or = 0
        s_and = 0
        t_and = 0

        for char in s:
            xor_num ^= ord(char)
            s_sum += ord(char)
            s_or |= ord(char)
            s_and &= ord(char)
        
        for char in t:
            xor_num ^= ord(char)
            t_sum += ord(char)
            t_or |= ord(char)
            t_and &= ord(char)

        return xor_num == 0 and s_sum == t_sum and s_or == t_or and s_and == t_and
        
    
def main():
    s = "dg"
    t = "ef"
    solution = Solution()
    print(solution.isAnagram2(s, t))

main()


