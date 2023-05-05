import numpy as np

tamanhos = 1_000, 10_000, 50_000, 100_000
for n in tamanhos:
    for i in range(3):
        vetor = np.random.randint(0, 1000, n)
        with open('vetor'+str(n)+'-'+str(i+1)+'.txt', 'w') as f:
            for number in vetor:
                f.write(str(number) + '\n')
            