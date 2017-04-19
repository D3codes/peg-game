import random
import board
import console
import time
import window

cross = 0.6
mutation = 0.01
pop_size = 250
chromo_length = 104
gene_length = 4
max_gens = 1000
gens = 0
DISPLAY_WINDOW = True

if DISPLAY_WINDOW:
    window.createWindow()

def replayBest(chromosome):
    splitUp = [chromosome[j:j+4] for j in range(0, len(chromosome), 4)]
    decoded = [int(byte, 2) for byte in splitUp]
    for j in range(0, 13, 2):
        if board.move(decoded[j], decoded[j+1]):
            console.printBoard()
    board.setBoard()

def fitness(population, bestChromo):
    didMove = True
    for i in range(0, len(population)):
        if didMove and DISPLAY_WINDOW:
            window.drawBoard()
        chromosome = population[i]['dna']
        splitUp = [chromosome[j:j+4] for j in range(0, len(chromosome), 4)]
        decoded = [int(byte, 2) for byte in splitUp]
        for j in range(0, 13, 2):
            if board.move(decoded[j], decoded[j+1]):
                population[i]['fitness'] += 104 - j
                if population[i]['fitness'] > bestChromo['fitness']:
                    bestChromo = population[i]
                console.printBoard()
        if board.wonGame():
            chromosome['won'] = True
            start = decoded[j]
            end = decoded[j+1]
            middle = board.middle(start, end)
            didMove = board.move(start, end)
            if didMove:
                population[i]['fitness'] += 1
                if DISPLAY_WINDOW:
                    window.fillPeg(start)
                    window.fillPeg(end)
                    window.fillPeg(middle)
        board.setBoard()
        console.println("Generation: " + str(gens) + " Genome: " + str(i) + " Fitness: " + str(population[i]['fitness']))
        #time.sleep(0.1)
    return bestChromo

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
        population[i] = {'dna': randomBits(chromo_length), 'fitness': 0, 'won': False}
    gens = 0
    best_chromosome = population[0]
    found = False

    while not found:
        best_chromosome = fitness(population, best_chromosome)
        for child in population:
            if child['won']:
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
            temp[i] = {'dna': offspring1, 'fitness': 0, 'won': False}
            temp[i+1] = {'dna': offspring2, 'fitness': 0, 'won': False}
        for i in range(0, pop_size):
            population[i] = temp[i]

        gens += 1
        if gens > max_gens:
            console.println("No solution found this run")
            console.println("Max fitness for this run: " + str(best_chromosome['fitness']))
            replayBest(best_chromosome['dna'])
            break

    if found:
        break
    if input("Again? : ")[0].upper() == 'Y':
        attempt += 1
    else:
        break
