import numpy as npy
import matplotlib.pyplot as mp
import lib_complejos as lb
import lib_complejos_extend as lbv

def quantum_mat_plot(vector,clic):
    print('El vector en el clic',clic,"es",vector)
    etiquetas = []
    est = []
    for i in range(len(vector)):
        etiquetas.append('Vertice '+str(i))
        est.append(lb.modulo_complejos(vector[i][0])**2)

    indicador = npy.arange(len(etiquetas))
    mp.bar(indicador, est)
    mp.xlabel('Estado')
    mp.ylabel('Vector')
    mp.xticks(indicador, etiquetas, rotation=45)
    mp.title('Evolución dinámica del sistema cuantico después de ' + str(clic) + ' clics de tiempo')
    mp.show()
