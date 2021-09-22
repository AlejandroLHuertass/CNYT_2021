import lib_complejos as lb
import lib_complejos_extend as lbv
import graficadora_normal as gn
import graficadora_cuantica as gc
import math

def multiplicacion_matriz(vector,matriz,clic):
    if clic == 0:
        return  vector
    elif clic == 1:
        return lbv.producto_Matriz(matriz,vector)
    else:
        return lbv.producto_Matriz(matriz,multiplicacion_matriz(vector,matriz,clic - 1))


def main():

    vector = input("Ingrese el vertice, por ejemplo a,b,c.. ").split(",")


    for i in range(len(vector)):
        vector[i] = [[int(vector[i]),0]]

    matriz = [ [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
            [[1/math.sqrt(2),0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
            [[1/math.sqrt(2),0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0]],
            [[0,0],[-1/math.sqrt(6),1/math.sqrt(6)],[0,0],[1,0],[0,0],[0,0],[0,0],[0,0]],
            [[0,0],[-1/math.sqrt(6),-1/math.sqrt(6)],[0,0],[0,0],[1,0],[0,0],[0,0],[0,0]],
            [[0,0],[1/math.sqrt(6),-1/math.sqrt(6)],[-1/math.sqrt(6),1/math.sqrt(6)],[0,0],[0,0],[1,0],[0,0],[0,0]],
            [[0,0],[0,0],[-1/math.sqrt(6),-1/math.sqrt(6)],[0,0],[0,0],[0,0],[1,0],[0,0]],
            [[0,0],[0,0],[1/math.sqrt(6),-1/math.sqrt(6)],[0,0],[0,0],[0,0],[0,0],[1,0]]
            ]

    for i in range(int(input("Ingrese numero de Clics"))):
  
        gc.quantum_mat_plot(multiplicacion_matriz(vector,matriz,i),i)
main()
