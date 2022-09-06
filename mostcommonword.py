import re
from typing import List
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=re.sub(r'[,.!?;\']',' ',paragraph)
        paragraph = paragraph.lower()
        s=paragraph.split()
        count=0
        word=""
        for i in list(set(s)):
            if s.count(i)>count and i not in banned:
                count=s.count(i)
                word =i
        return word