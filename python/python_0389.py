class Solution(object):

    # 1. hash 表
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        s_hash = {}
        t_hash = {}
        for char in s:
            if char in s_hash:
                s_hash[char] += 1
            else:
                s_hash[char] = 1

        for char in t:
            print(f's_hash: {s_hash}')
            if char not in s_hash:
                return char
            else:
                if char in t_hash:
                    t_hash[char] += 1
                else:
                    t_hash[char] = 1
            print(f't_hash: {t_hash}')
            if (t_hash[char] > s_hash[char]):
                return char
            
    # 2. ASCII码求差
    def findTheDifference2(self, s, t):
        s_sum = 0
        t_sum = 0
        for char in s:
            s_sum += ord(char)
        for char in t:
            t_sum += ord(char)
        return chr(t_sum - s_sum)
    
    # 3. 合并后找出出现奇数次的字符
    def findTheDifference3(self, s: str, t: str) -> str:
        tmp_str = s + t
        tmp_hash = {}
        for char in tmp_str:
            if char in tmp_hash:
                tmp_hash[char] += 1
            else:
                tmp_hash[char] = 1
        
        for char in tmp_hash:
            if (tmp_hash[char] % 2 == 1):
                return char

    # 4. 位运算
    def findTheDifference4(self, s: str, t: str) -> str:
        ret = 0
        for char in s:
            ret ^= ord(char)
            print(ret)
        
        for char in t:
            ret ^= ord(char)
            print(ret)
        
        return chr(ret)
        


def main():
    s = "abc"
    t = "bcaa"
    solution = Solution()
    print(solution.findTheDifference4(s, t))

if __name__ == "__main__":
    main()
