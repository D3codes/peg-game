import random
import board
import console
import time

cross = 0.7
mutation = 0.002
pop_size = 100
chromo_length = 104
gene_length = 4
max_gens = 5000
gens = 0

def fitness(population):
    for i in range(0, len(population)):
        chromosome = population[i]['dna']
        splitUp = [chromosome[j:j+4] for j in range(0, len(chromosome), 4)]
        decoded = [int(byte, 2) for byte in splitUp]
        for j in range(0, 13, 2):
            if board.move(decoded[j], decoded[j+1]):
                population[i]['fitness'] += 1
                console.printBoard()
        board.setBoard()
        console.println("Generation: " + str(gens) + " Genome: " + str(i) + " Fitness: " + str(population[i]['fitness']))
        #time.sleep(0.5)

def chooseParent(population):
    maximum = sum([child['fitness'] for child in population])
    pick = random.uniform(0, maximum)
    current = 0
    for child in population:
        current += child['fitness']
        if current >= pick:
            return child['dna']

def crossover(a, b):
    if random.uniform(0, 1) <= cross:
        length = len(a)
        gene = int(random.uniform(0, length))
        new_a = a[:gene] + b[gene:]
        new_b = b[:gene] + a[gene:]
        return[new_a, new_b]
    return[a, b]

def mutate(dna):
    new_dna = ""
    for bit in dna:
        if random.uniform(0, 1) <= mutation:
            if bit == '0':
                new_dna += '1'
            else:
                new_dna += '0'
        else:
            new_dna += bit
    return new_dna

def randomBits(length):
    bits = ""
    for i in range(0, length):
        if random.uniform(0, 1) > 0.5:
            bits += '1'
        else:
            bits += '0'
    return bits

attempt = 0
while True:
    print("Attempt #" + str(attempt))

    population = [None] * pop_size
    for i in range(0, pop_size):
        population[i] = {'dna': randomBits(chromo_length), 'fitness': 0}
    gens = 0
    found = False

    while not found:
        fitness(population)
        for child in population:
            if child['fitness'] == 13:
                console.println("Found solution: " + child['dna'])
                found = True
                break

        temp = [None] * pop_size
        for i in range(0, pop_size, 2):
            offspring1 = chooseParent(population)
            offspring2 = chooseParent(population)
            crsovr = crossover(offspring1, offspring2)
            offspring1 = crsovr[0]
            offspring2 = crsovr[1]
            offspring1 = mutate(offspring1)
            offspring2 = mutate(offspring2)
            temp[i] = {'dna': offspring1, 'fitness': 0}
            temp[i+1] = {'dna': offspring2, 'fitness': 0}
        for i in range(0, pop_size):
            population[i] = temp[i]

        gens += 1
        if gens > max_gens:
            console.println("No solution found this run")
            break

    if found:
        break
    attempt += 1
