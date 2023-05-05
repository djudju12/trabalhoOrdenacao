# Utilizar estas funcões para calcular quantidade de comparações e mudanças
from bisect import bisect_left

# _Algoritmos___________________________________________________________________

def shell_sort(alist):
    def gap_insertion_sort(alist,start,gap):
        for i in range(start+gap,len(alist),gap):

            currentvalue = alist[i]
            position = i

            while position>=gap and alist[position-gap]>currentvalue:
                alist[position]=alist[position-gap]
                position = position-gap

            alist[position]=currentvalue

    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
             gap_insertion_sort(alist,startposition,sublistcount)
        sublistcount = sublistcount // 2

    return alist

def bubble_sort(vetor):
    n = len(vetor)
    troca = True
    while troca:
        troca = False
        for i in range(n - 1):
            if vetor[i] > vetor[i + 1]:
                vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]
                troca = True
        n -= 1

    return vetor

def merge_sort(lista):
    if len(lista) > 1:
        meio = len(lista) // 2
        esquerda = lista[:meio]
        direita = lista[meio:]

        # Recursão para ordenar os subvetores esquerdo e direito
        esquerda = merge_sort(esquerda)
        direita = merge_sort(direita)

        # Mesclagem dos subvetores esquerdo e direito
        lista = []
        while esquerda and direita:
            if esquerda[0] <= direita[0]:
                lista.append(esquerda.pop(0))
            else:
                lista.append(direita.pop(0))

        # Adiciona os elementos restantes de esquerda e direita
        lista.extend(esquerda)
        lista.extend(direita)

    return lista

def index_sort(lista):
    # determina o valor máximo e mínimo da lista
    valor_maximo = max(lista)
    valor_minimo = min(lista)

    # Cria uma lista com um índice para cada valor possívl na array, 
    # considerando os valores máximos e mínimos
    contadores = [0] * (valor_maximo - valor_minimo + 1)
   
    # Conta a ocorrência de cada valor na lista
    for valor in lista:
        contadores[valor - valor_minimo] += 1

    # Constrói a lista ordenada
    lista_ordenada = []
    for valor in range(valor_minimo, valor_maximo + 1):
        indice = valor - valor_minimo
        # Adiciona o valor na lista ordenada, o valor é adicionado de acordo 
        # com a quantidade de vezes que ele aparece na lista original
        lista_ordenada.extend([valor] * contadores[indice])

    return lista_ordenada

def insertion_sort(vetor):
    for i in range(1, len(vetor)):
        chave = vetor[i]
        j = bisect_left(vetor, chave, 0, i)
        vetor[j+1:i+1] = vetor[j:i]
        vetor[j] = chave
    
    return vetor

def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr 


def particao(array, first, last):
    pivot = array[first]

    low = first + 1

    while True:

        while low <= last and array[low] <= pivot:
            low += 1

        while low <= last and array[last] >= pivot:
            last -= 1

        if last < low:
            break
        else:
            array[low], array[last] = array[last], array[low]

    array[first], array[last] = array[last], array[first]
    return last

def quick_sort(array, first=0, last=None):
    if last is None:
        last = len(array) - 1

    if first < last:
        split = particao(array, first, last)

        quick_sort(array, first, split - 1)
        quick_sort(array, split + 1, last)

    return array 

# ______________________________________________________________________________

# _Algoritmos de Comparação/Trocas______________________________________________
def merge_count(vetor):
    _, comparacoes, trocas = merge_count_impl(vetor)
    return comparacoes, trocas

def merge_count_impl(vetor):
    trocas = 0
    comparacoes = 0
    
    if len(vetor) > 1:
        meio = len(vetor) // 2
        esquerdo = vetor[:meio]
        direito = vetor[meio:]

        # recursão para ordenar os subvetores esquerdo e direito
        vetor_ordenado, comparacoes_esq, trocas_esq = merge_count_impl(esquerdo)
        vetor_ordenado, comparacoes_dir, trocas_dir = merge_count_impl(direito)


        trocas = trocas_esq + trocas_dir

        comparacoes = comparacoes_esq + comparacoes_dir

        i = j = 0
        vetor_ordenado = []

        # mesclagem dos subvetores esquerdo e direito
        while i < len(esquerdo) and j < len(direito):
            comparacoes += 1
            if esquerdo[i] <= direito[j]:
                vetor_ordenado.append(esquerdo[i])
                i += 1
            else:
                vetor_ordenado.append(direito[j])
                j += 1
                trocas += len(esquerdo) - i

        # adiciona os elementos restantes de esquerdo e direito
        vetor_ordenado += esquerdo[i:]
        vetor_ordenado += direito[j:]

        return vetor_ordenado, comparacoes, trocas

    else:
        return vetor, 0, 0

def index_count(arr):
    return 0, 0

def selection_count(arr):
    comparacoes = 0
    trocas = 0
    for i in range(len(arr)):
        min_index = i
        for j in range(i+1, len(arr)):
            comparacoes += 1
            if arr[j] < arr[min_index]:
                min_index = j
        trocas += 2
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return comparacoes, trocas

def particao_for_counting(array, first, last):
    comparisons = 0
    changes = 0

    pivot = array[first]

    low = first + 1
    high = last

    while True:

        while low <= high and array[low] <= pivot:
            low += 1
            comparisons += 2

        while low <= high and array[high] >= pivot:
            high -= 1
            comparisons += 2

        comparisons += 1
        if high < low:
            break
        else:
            array[low], array[high] = array[high], array[low]
            changes += 2

    array[first], array[high] = array[high], array[first]
    changes += 2
    return high, comparisons, changes


def quick_count(array, first=0, last=None, comparisons=0, changes=0):

    comparisons += 1
    if last is None:
        last = len(array) - 1

    comparisons += 1
    if first < last:
        split, comparisons, changes = particao_for_counting(array, 
                                                            first, 
                                                            last)

        cl, tl = quick_count(array, first, split - 1, comparisons, changes)
        cr, tr = quick_count(array, split + 1, last, comparisons, changes)

        comparisons += cr + cl
        changes += tl + tr

    return comparisons, changes

def insertion_count(vetor):
    changes = 0
    comparisons = 0                           
    for i in range(1, len(vetor)):
        chave = vetor[i]

        j = bisect_left(vetor, chave, 0, i)
        # incrementa a contagem de comparações
        comparisons += i - j                  

        if j != i:
            changes += 1

        vetor[j+1:i+1] = vetor[j:i]
        vetor[j] = chave
    
    return comparisons, changes

def bubble_count(vetor):
    n = len(vetor)
    troca = True
    conta_trocas = 0 
    conta_comparacoes = 0
    while troca:
        troca = False
        for i in range(n - 1):
            if vetor[i] > vetor[i + 1]:
                vetor[i], vetor[i + 1] = vetor[i + 1], vetor[i]
                troca = True
                conta_trocas += 1
            conta_comparacoes += 1
        n -= 1

    return conta_comparacoes, conta_trocas

def shell_count(alist):
    comparacoes = 0
    swaps = 0

    def gap_insertion_sort(alist,start,gap):
        c = 0 
        s = 0 
        for i in range(start+gap,len(alist),gap):

            currentvalue = alist[i]
            position = i

            while position>=gap and alist[position-gap]>currentvalue:
                alist[position]=alist[position-gap]
                position = position-gap
                c += 1
                s += 1

            c += 1
            alist[position]=currentvalue
        return c, s

    sublistcount = len(alist)//2
    while sublistcount > 0:

        for startposition in range(sublistcount):
            ct, st = gap_insertion_sort(alist,startposition,sublistcount)
            comparacoes += ct
            swaps += st
        sublistcount = sublistcount // 2

    return comparacoes, swaps
# ______________________________________________________________________________
