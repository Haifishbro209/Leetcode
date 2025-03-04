class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = None
        for s in range(len(strs)):
            for l in range(len(strs[s])):

                        
