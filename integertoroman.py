class Solution:
    def intToRoman(self, num: int) -> str:
        n=[1,4,5,9,10,40,50,90,100,400,500,900,1000]
        rom=["I","IV","V","IX","X","XL","L","XC","C","CD","D","CM","M"]
        i=12
        string=""
        while num:
            div=num//n[i]
            num%=n[i]
            while div:
                string+=rom[i]
                div-=1
            i-=1
        return string