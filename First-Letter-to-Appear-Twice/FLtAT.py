
class Solution:
    def repeatedCharacter(self, s: str) -> str:

        
        longitud_comprobacion = 0
        cantidad_de_iteraciones = len(s)

        
        def comprobacion(s,longitud_comprobacion, cantidad_de_iteraciones):

            longitud_comprobacion += 1
            cantidad_de_iteraciones -= 1

            for i in range(0,cantidad_de_iteraciones):
                
                #realizo comprobacion
                if s[i] == s[i+longitud_comprobacion]:
                    return s[i]

            comprobacion(s,longitud_comprobacion,cantidad_de_iteraciones)

        comprobacion(s,longitud_comprobacion,cantidad_de_iteraciones)