import random
import basic_math as bs_math
import numpy as np

POPULATION_SIZE = int(10)
GENERATIONS = int(100)
MUTATION_RATE = 0.05

def gen_initial_pop(N_cities:int, population_size:int = POPULATION_SIZE) -> list:
    population_ = []

    base_ = list(range(N_cities))
    for _ in range(population_size):
        initial_ = base_.copy()
        random.shuffle(initial_)
        population_.append(initial_)

    return population_

def fitness(path:list[int], points:list[list[int]]) -> float:
    path_length = bs_math.calc_path_length(path, points)
    if path_length == 0:
        return float('inf')
    
    return (1 / path_length)

def tournament_selection(population_points:list[list[int]], points:list[list[int]], k_numOfPaths:int = 3):
    selected = random.sample(population_points, k_numOfPaths)
    best = max(selected, key=lambda path: fitness(path, points))

    return best

# Order Crossover (OX)
def crossover(parent1:list[int], parent2:list[int]) -> list[int]:
    size_ = len(parent1)
    child = [None] * size_

    # cutting points
    start, end = sorted(random.sample(range(size_), 2))

    # grab the pieces from the 1st parent
    child[start:end+1] = parent1[start:end+1]

    # grab the missing points from the 2nd parent
    parent2_index = 0
    for i in range(size_):
        if child[i] is None:
            while parent2[parent2_index] in child:
                parent2_index += 1
            
            child[i] = parent2[parent2_index]

    return child

# Swap mutation
def mutate(path:list[int], mutation_rate:float = MUTATION_RATE) -> list[int]:
    new_path = path.copy()
    if random.random() < mutation_rate:
        i, j = random.sample(range(len(path)), 2)
        new_path[i], new_path[j] = new_path[j], new_path[i]

    return new_path

def genetic_algorithm(content:dict, population_size:int = POPULATION_SIZE, generations:int = GENERATIONS, mutation_rate:float = MUTATION_RATE):
    # 1.) enerate population
    population = gen_initial_pop(content["N"], population_size=population_size)
    points = content["points"]

    best_path = None
    best_length = float('inf')

    for gen in range(generations):
        # 2.) Calculate fitness
        fitness_scores = [bs_math.calc_path_length(individual, points) for individual in population]

        # get the best 3 individuals and fitness (Elitism)
        sorted_indices = np.argsort(fitness_scores)
        best_individuals = [population[i].copy() for i in sorted_indices[:3]]

        # get the best one
        for i in range(population_size):
            if fitness_scores[i] < best_length:
                best_length = fitness_scores[i]
                best_path = population[i]

        # create new population containing the best individuals (Elitism)
        new_population = best_individuals.copy()

        # 3.) Create new population
        while len(new_population) < population_size:
            # 3.1) choose parents
            parent1 = tournament_selection(population, points)
            parent2 = tournament_selection(population, points)
            
            # 3.2) create child
            child = crossover(parent1, parent2)

            # 3.3) mutate
            child = mutate(child, mutation_rate=mutation_rate)

            # 3.4) add child to new population
            new_population.append(child)

        population = new_population
        print(f'[Gen {gen}.] The best path length so far: {best_length:.4f}')

    return best_length, best_path