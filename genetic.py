import random
import board
import console
import time
import window

cross = 0.6
mutation = 0.01
pop_size = 100
chromo_length = 416
max_gens = 4000
DISPLAY_WINDOW = False

gens = 0
gene_length = 4
numberOfMoves = int(chromo_length/gene_length)
MAX_FITNESS = 13
SUCCESSES = 0
successful_chromos = []

if DISPLAY_WINDOW:
    window.createWindow()

def saveSuccesses():
    target = open("successes.txt", 'a')
    target.truncate()
    for dna in successful_chromos:
        target.write(str(dna) + '\n')
    target.close()

def readSuccesses():
    target = open("successes.txt", 'r')
    target.truncate()
    for line in target:
        successful_chromos.append(line)
    target.close()

def replayBest(chromosome):
    splitUp = [chromosome[j:j+4] for j in range(0, len(chromosome), 4)]
    decoded = [int(byte, 2) for byte in splitUp]
    for j in range(0, int(chromo_length/gene_length), 2):
        if board.move(decoded[j], decoded[j+1]):
            window.drawBoard()
            time.sleep(0.6)
    board.setBoard()

def fitness(population, bestChromo):
    didMove = True
    for i in range(0, len(population)):
        if didMove and DISPLAY_WINDOW:
            window.drawBoard()

        chromosome = population[i]['dna']
        splitUp = [chromosome[j:j+4] for j in range(0, len(chromosome), 4)]
        decoded = [int(byte, 2) for byte in splitUp]
        for j in range(0, numberOfMoves, 2):
            start = decoded[j]
            end = decoded[j+1]
            middle = board.middle(start, end)
            didMove = board.move(start, end)
            if didMove:
                if DISPLAY_WINDOW:
                    window.fillPeg(start)
                    window.fillPeg(end)
                    window.fillPeg(middle)
        population[i]['fitness'] = MAX_FITNESS - (board.pegsRemaining() - 1)
        if population[i]['fitness'] > bestChromo['fitness']:
            bestChromo = population[i]

        if board.wonGame():
            population[i]['won'] = True
            successful_chromos.append(population[i]['dna'])

        board.setBoard()
        #console.println("Generation: " + str(gens) + " Genome: " + str(i) + " Fitness: " + str(population[i]['fitness']) + "/" + str(MAX_FITNESS))
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

#def scramble(dna):


def randomBits(length):
    bits = ""
    for i in range(0, length):
        if random.uniform(0, 1) > 0.5:
            bits += '1'
        else:
            bits += '0'
    return bits

attempt = 1
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
        if gens % 1000 == 0:
            console.println("\tGeneration: " + str(gens))
        if gens > max_gens:
            console.println("\tNo solution found this run")
            console.println("\tMax fitness for this run: " + str(best_chromosome['fitness']) + '/' + str(MAX_FITNESS))
            replayBest(best_chromosome['dna'])
            break

    if found:
        replayBest(best_chromosome['dna'])
        SUCCESSES += 1
        break
    #if input("Again? : ")[0].upper() == 'Y':
    attempt += 1
    console.println("\tSuccesses: " + str(SUCCESSES))
    #else:
    #    break
console.println("Saving successes")
saveSuccesses()
