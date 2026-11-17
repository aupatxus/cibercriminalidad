
import variables 

import h1 
import h2
import h3
import h4
import h5


    
print("\n\n\nAnálisis de la evolución de los ciberdelitos y situación de la cibercriminalidad")
print("================================================================================\n")

try:

    print("\nProcesando la hipótesis 1")
    print("-------------------------")
    h1.h1()
    print("\nProcesando la hipótesis 2")
    print("-------------------------")
    h2.h2()
    print("\nProcesando la hipótesis 3")
    print("-------------------------")
    h3.h3()
    print("\nProcesando la hipótesis 4")
    print("-------------------------")
    h4.h4()
    print("\nProcesando la hipótesis 5")
    print("-------------------------")
    h5.h5()
    
except FileNotFoundError as e:
    print("\nERROR", e)
except KeyError as e:
    print("\nERROR", e)

print("\nLa ejecución del script para el Análisis de la evolución de los ciberdelitos y situación de la cibercriminalidad ha finalizado.\n")

