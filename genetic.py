import random

global crossover = 0.7
global mutation = 0.001
global pop_size = 100
global chromo_length = 104
global gene_length = 4
global max_gens = 400

def fitness(population):
    for child in population:
        chromosome = child.dna
        splitUp = [chromosome[i:i+4] for i in range(0, len(chromosome), 4)]
        decoded = [int(byte, 2) for byte in splitUp]


def chooseParent(population):
    max = sum([child.fitness for child in population])
    pick = random.uniform(0, max)
    current = 0
    for child in population:
        current += child.fitness
        if current > pick:
            return child

def crossover(parents):
    if random.uniform(0, 1) <= crossover:
        length = len(parents.a.dna)
        gene = random.uniform(0, length)
        temp = parents.a.dna[gene:length]
        parents.a.dna[gene:length] = parents.b.dna[gene:length]
        parents.b.dna = temp
    return parents

def mutation(population):
    for child in population:
        for gene in child.dna:
            if random.uniform(0, 1) <= mutation:
                if gene == '0':
                    gene = '1'
                else:
                    gene = '0'
    return population

while True:
    population = []
    for i in pop_size:
        population[i].dna =
