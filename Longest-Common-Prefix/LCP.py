from typing import List
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        respuesta = ""
        length = (len(strs))
        if length == 1:
            return("")
        #este for si es 6 va de 0 a 5
        #esta perfecto
        for j in range(0,(len(strs[0]))):

            counter = 0
            #bien el for
            for i in range(1,length):

                if j < len(strs[i]):
                    if strs[0][j] == strs[i][j]:
                        counter +=1

            if counter == length-1:
                respuesta = respuesta + strs[0][j]
            else:
                return(respuesta)
                break
        return(respuesta)

lista = ["f","flo","flight"]
solucion = Solution()
print(solucion.longestCommonPrefix(lista))
