from os import walk
import os




def verificaNomesDosArquivos():
    thisPath = './'
    f = []
    for (dirpath, dirnames, filenames) in walk(thisPath):
        f.extend(filenames)
        break
    return f


def apagaArquivo(nomeDoArquivo):
    dir = os.listdir('./')
    for file in dir:
        if file == nomeDoArquivo:
            os.remove(nomeDoArquivo)
            print("O arquivo ",nomeDoArquivo," foi apagado!")

def verificaNumeroDeLinhasNoCSV(nomeDoArquivo):
    dados = []
    arquivo = open(nomeDoArquivo);
    numeroDeLinhas = sum(1 for row in arquivo);
    return(numeroDeLinhas)

def start():
    contadorDeExclusoes = 0
    listaDeArquivos = verificaNomesDosArquivos();
    for nomeDoArquivo in listaDeArquivos:
        if (verificaNumeroDeLinhasNoCSV(nomeDoArquivo) == 1):
            apagaArquivo(nomeDoArquivo)
            contadorDeExclusoes += 1
    print(contadorDeExclusoes," Registros foram Apagados")
        

start()
