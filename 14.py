class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        arr = []
        strs = ["flower","flow","flight"]

        for l in range(len(min(strs,key = len))):
            objs = []
            for string in strs:
                objs.append(string[l])
            for objec in range(len(objs)):
                if objec != 0:
                    if objs[objec] != objs[objec -1]:
                        return prefix
            if l == len(min(strs,key = len))-1:
                prefix = prefix + objs[0] 
        return prefix
