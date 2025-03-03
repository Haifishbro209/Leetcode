class Solution:
    def romanToInt(self, s: str) -> int:
        dictonary = {
            "I":1,
            "V":5,            
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        num = 0
        for l in range(len(s)):
            num += dictonary[s[l]]
            if l != 0:
                if dictonary[s[l-1]] < dictonary[s[l]] :
                    num-= 2 * dictonary[s[l-1]]
                
        return num
