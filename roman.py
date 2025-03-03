def romanToInt(s):
    I = 1
    V = 5
    X = 10
    L = 50
    C = 100
    D = 500
    M = 1000
    num = 0
    for l in range(len(s)):
        match s[l]:
            case "I":
                num += I
            case "V":
                if l != 0:
                    if s[l-1] == "I":
                        num += (V-I)
                    else:
                       num += V
                else:
                    num += V
            case "X":
                if l != 0:
                    if s[l-1] == "I":
                        num += (X-I)
                    else:
                       num += X
                else:
                    num += X            
            case "L":
                if l != 0:
                    if s[l-1] == "X":
                        num += (L-X)
                    else:
                       num += L
                else:
                    num += L 
            case "C":
                if l != 0:
                    if s[l-1] == "X":
                        num += (C-X)
                    else:
                       num += C
                else:
                    num += C 
            case "D":
                if l != 0:
                    if s[l-1] == "C":
                        num += (D-C)
                    else:
                       num += D
                else:
                    num += D 
            case "M":
                if l != 0:
                    if s[l-1] == "C":
                        num += (M-C)
                    else:
                       num += M
                else:
                    num += M 
        return num
print(romanToInt("IV"))




class Solution2:
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
                if s[l-1] == "I":
                    num += (V-I)
                else:
                    num += V
            else:
                num += V
        return num
