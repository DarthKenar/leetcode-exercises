from typing import List


class Solution:
    def repeatedCharacter(self, s: str) -> str:

        #la comprobacion debe disminuír en 1
        
        longitud_comprobacion = 0
        cantidad_de_iteraciones = len(s)-1

        def comprobacion(s: List(str),longitud_comprobacion: int, cantidad_de_iteraciones: int):

            longitud_comprobacion += 1
            cantidad_de_iteraciones = len(s)-1

            for i in range(0,cantidad_de_iteraciones):
                
                #realizo comprobacion
                if s[i] == s[i+longitud_comprobacion]:
                    return s[i]

            comprobacion(s,longitud_comprobacion,i)
        
        #comprobacion(s,longitud_comprobacion,i)