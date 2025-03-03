def longestCommonPrefix( strs) -> str:
        prefix = None
        for l in range(200):
                arr = []
                for string in range(len(strs)):
                        try:
                                print(strs[string][l])
                                arr.append(strs[string][l])
                                if string !=0:
                                    if arr[string] != arr[string-1]:
                                           break
                                    else:
                                           prefix = arr[string]
                        except:
                                pass
                
        '''for i in range(len(strs)):
            for letter in strs[i]:
                print(letter)'''
#print(longestCommonPrefix(["flower","flow","flight"]))
longestCommonPrefix(["flower","flow","flight"])
