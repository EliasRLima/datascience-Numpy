import numpy as np
from numpy import arange

def main():
    
    km = np.array([1000, 2300, 4987, 1500])
    print(km)

    km = np.loadtxt(fname = "data\\carros-km.txt")
    print(km.dtype)
    km = np.loadtxt(fname = "data\\carros-km.txt", dtype = int)
    print(km.dtype)
    print(km)
    print(km.shape) #tupla com as dimensões do array

    np_array = np.arange(1000000)
    py_list = list(range(1000000))

    for _ in range(100): np_array *= 2 # %time - CPU times: user 65.2 ms, sys: 0 ns, total: 65.2 ms Wall time: 73.7 ms
    for _ in range(100): py_list = [x * 2 for x in py_list] # %time - CPU times: user 8.17 s, sys: 1.79 s, total: 9.96 s Wall time: 9.98 s
    #range +10 vs arange numpy

    contador = np.arange(10)
    print(contador)

    item = 6
    index = item - 1
    print(contador[index])
    print(contador[-1])

    km = np.array([44410., 5712., 37123., 0., 25757.])
    anos = np.array([2003, 1991, 1990, 2019, 2006])
    dados = np.array([km, anos])
    print(dados)

    print(dados[1][2])
    print(dados[1,2])

    print(contador[1:4]) #esse array se inicia com 0 e queremos selecionar os valores 1, 2 e 3
    print(contador[1:8:2]) #vamos varrer o array contador do índice 1 até o 8, que não será incluído, contando dois passos a cada elemento encontrado.

    print(contador[::2]) #somente pares
    print(contador[1::2]) #somente impares

    contador = np.arange(10)
    print(contador)
    print(contador[contador >5]) #array([6, 7, 8, 9])
    print(contador[[False, False, False, False, False, False,  True,  True,  True, True]])

    dados = np.array(
    [
        ['Roberto', 'casado', 'masculino'],
        ['Sheila', 'solteiro', 'feminino'],
        ['Bruno', 'solteiro', 'masculino'],
        ['Rita', 'casado', 'feminino']
    ]
    )

    #somente sexo masculino
    print(dados[0::2, :2]) #array([['Roberto', 'casado'],['Bruno', 'solteiro']], dtype='<U9')

    contador = np.arange(10)
    print(contador) #array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

    print(contador.reshape((5,2))) #array([[0, 1], [2, 3], [4, 5], [6, 7], [8, 9]])  

    anos = np.loadtxt(fname = "data\\carros-anos.txt", dtype = int)
    valor = np.loadtxt(fname = "data\\carros-valor.txt")
    km = np.loadtxt(fname = "data\\carros-km.txt", dtype = int)
    dataset = np.column_stack((anos, km, valor))
    print(dataset)
    print(dataset.shape)

    #media
    print(np.mean(dataset)) #calculando a média de todos os anos, quilometragens e valores juntos
    print(np.mean(dataset, axis = 0)) #média das colunas
    idades = np.array([10, 23, 45, 34, 25])
    print(idades.mean()) #outra forma de calcular a media
    print(np.sum(idades) / idades.size) #somatoria/tamanho = media

    #desvio padrão dos valores
    print(np.std(dataset[:,2])) 
    #29754.101150388564

    #somatória dos valores do array
    print(np.sum(dataset[:, 2])) # 25531812.38
    print(dataset.sum(axis = 0)) #passando o eixo
    #array([ 517938. , 11480849. , 25531812.37999999])

if(__name__ == "__main__"):
    main()