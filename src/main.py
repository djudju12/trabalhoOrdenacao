from collections.abc import Callable
import csv
import datetime
import os
from algoritmosPerformance import *

# _DEFINIÇÃO DAS VARIAVEIS_______________________________________________________
PARENT_FOLDER = r'vetores2'

# Funções de tempo
ALGORITMOS_TIME: list[Callable] = [quick_time, merge_time, 
                                   selection_time, insertion_time, 
                                   index_time]

# Funções de troca e comparação
ALGORITMOS_COUNT: list[Callable] = [quick_count, merge_count, 
                                    selection_count, insertion_count, 
                                    index_count]

# Path do arquivo que conterá os resultados
PATH_RESULTADO = 'resultados.csv'

# Cabeçalho do arquivo com os resultados
HEADER = ['Algoritmo', 'Cenario', 'Trocas', 'Comparacoes', 'Tempo']

def main() -> None:
    # Criar todos os vetores (pequeno, medio, grande, supergrande)
    vetores = criar_vetores()

    # Começa os testes e printa a hora
    print('start: ', hora_agora())
    with open(PATH_RESULTADO, 'w', newline='') as f:

        # csv.writer() é o objeto que escreverá no arquvio de resultado
        writer = csv.writer(f, delimiter='|')
        writer.writerow(HEADER)

        # Itera sobre cada um dos algoritmos de tempo e comparação/troca
        # zip coloca o elemento n de cada uma das listas em uma tupla 
        for algo_time, algo_count in zip(ALGORITMOS_TIME, ALGORITMOS_COUNT):
            # As chaves são os cenarios. Ex vetor1000-1, vetor1000-2, vetor1000-3
            for cenario in vetores.keys():
                # retorna duas copias do vetor que sera testado
                vetor_time, vetor_count = make_2_copies(vetores[cenario]) 
                
                # calcula comparação e trocas
                comparacoes, trocas = algo_count(vetor_count)
                
                # calcula tempo
                tempo = algo_time(vetor_time)
                
                # escreve no arquivo o nome do algoritmo e os resultados 
                # Usei só o nome do algoritmo de tempo pq nao era necessário 
                # um nome separado para o de comparaçao/troca
                writer.writerow([algo_time.__name__, cenario, 
                                 str(trocas), str(comparacoes), 
                                 str(tempo)])

                # Quando termina um cenário printa o a hora, algoritmo e cenario
                print(f'{hora_agora()}: ', algo_time.__name__, cenario)

    # fim
    print('End: ', hora_agora())

def make_2_copies(vetor: list) -> tuple[list, list]:
    return vetor.copy(), vetor.copy() 

# Retorna a hora atual em hora:minuto:segundo
def hora_agora() -> str:
    return datetime.datetime.now().strftime('%H:%M:%S')


def criar_vetores() -> dict[str, list]:
    vetores = {}
    
    # Lê todos os arquvios que estão no path PARENT_FOLDER
    for vetor_path in sorted(os.listdir(PARENT_FOLDER)):
        
        # Pega só o nome junto da extensão
        _, file_name = os.path.split(vetor_path)
        with open(os.path.join(PARENT_FOLDER, vetor_path), 'r') as f:
            
            # Splita na quebras de linha
            vetor = list(map(int, f.read().split('\n')))

            # Adciona o vetor no dicionario e a chave sera o nome do arquivo
            # sem a extensão. O nome dos arquivos possuem o padrão vetor + tamanho + nº cenario
            vetores[file_name[:-4]] = vetor
    return vetores


if __name__ == '__main__':
    main()