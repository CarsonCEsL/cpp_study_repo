class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return s in (s + s)[1:-1]
    
def main():
    print(Solution().repeatedSubstringPattern("abab"))
    print(Solution().repeatedSubstringPattern("aba"))
    print(Solution().repeatedSubstringPattern("a"))
    print(Solution().repeatedSubstringPattern("aa"))

main()
