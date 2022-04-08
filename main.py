import numpy as np

def main():
    km = np.loadtxt('data\\carros-km.txt')
    anos = np.loadtxt('data\\carros-anos.txt')
    
    km_media = km / (2022 - anos) #quantos km os carros rodaram em media por ano
    print(km_media)


if(__name__ == "__main__"):
    main()