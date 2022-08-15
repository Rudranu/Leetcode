class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        str1=[]
        str1=s.split()
        return len(str1[-1])