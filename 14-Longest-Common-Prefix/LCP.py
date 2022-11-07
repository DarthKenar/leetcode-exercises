class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        target = ""
        size = (len(strs))
        if size == 1:

            return(strs[0])

        for j in range(0,(len(strs[0]))):

            counter = 0

            for i in range(1,size):

                if j < len(strs[i]):

                    if strs[0][j] == strs[i][j]:

                        counter +=1

            if counter == size-1:

                target = target + strs[0][j]

            else:

                return(target)
            
        return(target)