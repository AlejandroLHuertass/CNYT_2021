import numpy as npy
import matplotlib.pyplot as mp
import lib_complejos as lb
import lib_complejos_extend as lbv

def mat_plot(vector,clic):
    print('El vector en el clic',clic,"es",vector)
    etiquetas = []
    est = []
    for i in range(len(vector)):
        etiquetas.append('Vertice '+str(i))
        est.append(vector[i][0][0])

    indicador = npy.arange(len(etiquetas))
    mp.bar(indicador, est)
    mp.xlabel('Estado')
    mp.ylabel('Vector')
    mp.xticks(indicador, etiquetas, rotation=45)
    mp.title('Evolución dinámica del sistema después de ' + str(clic) + ' clics de tiempo')
    mp.show()
