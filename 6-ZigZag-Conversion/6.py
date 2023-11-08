class Solution:
    def convert(self, s: str, numRows: int) -> str:
        
        if numRows == 1:
            return s

        index = []
        zigzag = True
        counter = 0

        for i in range(len(s)):

            if zigzag == True:
                
                index.append(counter)
                counter += 1

                if counter == numRows-1:

                    zigzag = False

            else:
                
                
                index.append(counter)
                counter -= 1
                if counter == 0:

                    zigzag = True
        
        counter = 0
        output = ""

        for i in range(len(s)):
            
            if counter in index:

                output = output + s[index.index(counter)]
                index[index.index(counter)] = "-"
                
            else:

                counter += 1
                output = output + s[index.index(counter)]
                index[index.index(counter)] = "-"
        
        return output

if __name__ == "__main__":

    a = Solution()
    print(a.convert("PAYPALISHIRING",4))#"PINALSIGYAHRPI"