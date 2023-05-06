from collections.abc import Callable
import csv
import datetime
import os
from algoritmosPerformance import *
from time import perf_counter

# _VARAVEIS GLOBAIS______________________________________________________________

PARENT_FOLDER = r'vetores2'

# Funções de tempo
ALGORITMOS: list[Callable] = [quick_sort, merge_sort,
                              selection_sort, insertion_sort,
                              index_sort, bubble_sort, shell_sort]

# Funções de troca e comparação
ALGORITMOS_COUNT: list[Callable] = [quick_count, merge_count,
                                    selection_count, insertion_count,
                                    index_count, bubble_count, shell_count]

# Path do arquivo que conterá os resultados
PATH_RESULTADO = 'resultados.csv'

# Cabeçalho do arquivo com os resultados
HEADER = ['Algoritmo', 'Cenario', 'Trocas', 'Comparacoes', 'Tempo']
# _______________________________________________________________________________

def main() -> None:
    # Criar todos os vetores (pequeno, medio, grande, supergrande)
    vetores = criar_vetores()

    # Começa os testes e printa a hora
    print('start: ', hora_agora())
    with open(PATH_RESULTADO, 'w', newline='') as f:

        # csv.writer() é o objeto que escreverá no arquvio de resultado
        writer = csv.writer(f, delimiter='|')
        writer.writerow(HEADER)

        n = 0
        a = (len(vetores) * len(ALGORITMOS)) // 2

        # Itera sobre cada um dos algoritmos de tempo e comparação/troca
        # zip coloca o elemento n de cada uma das listas em uma tupla 
        concluidos = []
        for algoritmo, algoritmo_count in zip(ALGORITMOS, ALGORITMOS_COUNT):
            # As chaves são os cenarios. Ex vetor1000-1, vetor1000-2...
            for cenario in vetores.keys():
                n += 1
                # bar(n, a, hora_agora(), algoritmo.__name__, cenario, ALGORITMOS,concluidos)
                bar(n, a, ALGORITMOS, concluidos)
                
                # Quando começa um cenário printa o a hora, algoritmo e cenario
                # print(f'{hora_agora()}:', algoritmo.__name__, cenario)
                
                # retorna duas copias do vetor que sera testado
                vetor_time, vetor_count = make_2_copies(vetores[cenario]) 
                
                # calcula comparação e trocas
                comparacoes, trocas = algoritmo_count(vetor_count)
                
                # calcula tempo
                time_s = perf_counter()
                vetor_ordenado = algoritmo(vetor_time)
                tempo = perf_counter() - time_s

                # Para verificar se os vetores estão ordenados
                # Não é necessario no teste final
                # if is_not_sorted(vetores[cenario], vetor_ordenado):
                #     print('ERRO NO ALGORITMO =>', algoritmo.__name__ )

                # escreve no arquivo o nome do algoritmo e os resultados 
                writer.writerow([algoritmo.__name__, cenario, 
                                 str(trocas), str(comparacoes), 
                                 str(tempo)])

            concluidos.append(algoritmo.__name__)

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
            # sem a extensão. O nome dos arquivos possuem o padrão 
            # vetor + tamanho + nº cenario
            vetores[file_name[:-4]] = vetor
    return vetores

def is_not_sorted(vetor: list, vetor_ordenado: list) -> bool:
    return sorted(vetor.copy()) != vetor_ordenado

# def bar(posicao, tamanho, hora, atual, cenario, lista_algoritmos: list, concluidos: list):
def bar(posicao, tamanho, lista_algoritmos: list, concluidos: list):
    # string = f'[{"*"*posicao+"~"*(tamanho-posicao)}]'
    string = f'[{"~"*posicao+">"+" "*(tamanho-posicao)}]'
    # os.system('cls')
    print('\033c')
    print(string)
    print_list(lista_algoritmos, concluidos)


def print_list(lista_algoritmos: list, concluidos: list):
    for item in lista_algoritmos:
        print(f'[{"x" if item.__name__ in concluidos else " "}] {item.__name__}')

if __name__ == '__main__':
    main()