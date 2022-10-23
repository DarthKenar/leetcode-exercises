class Solution:
    def repeatedCharacter(self, s: str) -> str:

        length_checkout = 0
        iteration_counter = len(s)

        
        def checkout(s,length_checkout, iteration_counter):

            length_checkout += 1
            iteration_counter -= 1

            for i in range(0,iteration_counter):
                
                if s[i] == s[i+length_checkout]:
                    return s[i]

            return(checkout(s,length_checkout,iteration_counter))

        return(checkout(s,length_checkout,iteration_counter))