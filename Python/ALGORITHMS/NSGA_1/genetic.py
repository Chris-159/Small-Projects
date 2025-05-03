import random
import pareto

POPULATION_SIZE = int(100)
MUTATION_RATE = 0.05
GENERATIONS = int(10)
TOTAL_PIECES = int(10)

def gen_initial_pop(N_workers:int, total_pieces:int = TOTAL_PIECES, population_size:int = POPULATION_SIZE) -> list:
    population_ = []

    for _ in range(population_size):
        assignment = [0] * N_workers
        remaining_pieces = total_pieces

        while remaining_pieces > 0:
            worker = random.randint(0, N_workers - 1)
            assignment[worker] += 1
            remaining_pieces -= 1
        
        population_.append(assignment)

    return population_

def fitness(individual:list[int], workers:list[tuple[float, float]]) -> tuple[float, float]:
    total_cost = 0
    total_error = 0

    for (wage, error_rate), pieces in zip(workers, individual):
        total_cost += wage * pieces
        total_error += error_rate * pieces

    return (total_cost, total_error)

def fitness_eval(population:list[list[int]], workers:list[tuple[float, float]]) -> list[tuple[float, float]]:
    fitnesses_ = []
    for i in range(len(population)):
        fitnesses_.append(fitness(population[i], workers))

    return fitnesses_

def tournament_selection(population:list[list[int]], fitnesses:list[tuple[float, float]], k_numOfWorkers:int = 3) -> list[int]:
    selected_slices = random.sample(range(len(population)), k_numOfWorkers)
    selected = [(population[i], fitnesses[i]) for i in selected_slices]

    non_dominated = [ind for ind in selected if not any(pareto.dominates(other[1], ind[1]) for other in selected if other != ind)]

    return random.choice(non_dominated)[0]

# Order Crossover (OX)
def crossover(parent1:list[int], parent2:list[int], total_pieces:int = TOTAL_PIECES) -> list[int]:
    child_ = [(p1 + p2) // 2 for p1, p2 in zip(parent1, parent2)]

    diff = total_pieces - sum(child_)
    for _ in range(abs(diff)):
        idx = random.randint(0, len(child_) - 1)
        if diff > 0:
            child_[idx] += 1 #if diff > 0 else -1
        elif child_[idx] > 0:
            child_[idx] -= 1

    return child_

# Swap mutation
def mutate(individual:list[int], mutation_rate:float = MUTATION_RATE) -> list[int]:
    mutated_ = individual.copy()
    
    for i in range(len(mutated_)):
        if random.random() < mutation_rate:
            j = random.randint(0, len(mutated_) - 1)
            if mutated_[i] > 0:
                mutated_[i] -= 1
                mutated_[j] += 1
    
    # if random.random() < mutation_rate:
    #     i, j = random.sample(range(len(mutated_)), 2)
    #     if mutated_[i] > 0:
    #         mutated_[i] -= 1
    #         mutated_[j] += 1

    return mutated_

def genetic_algorithm(content:dict, population_size:int = POPULATION_SIZE, generations:int = GENERATIONS, mutation_rate:float = MUTATION_RATE) -> list[tuple[list[int], tuple[float, float]]]:
    # 1.) generate population
    population = gen_initial_pop(content["N"], population_size=population_size)
    workers = content["workers"]

    for gen in range(generations):
        # 2.) Calculate fitness
        fitnesses = fitness_eval(population, workers)

        # 3.) Get Pareto-front (Elitism)
        front = pareto.get_front(population, fitnesses)
        front_individuals = [ind for ind, fit in front]

        # 4.) Create new population (keep Pareto elitism)
        new_population = front_individuals.copy()

        while len(new_population) < population_size:
            # 4.1) choose parents
            parent1 = tournament_selection(population, fitnesses)
            parent2 = tournament_selection(population, fitnesses)
            
            # 4.2) create child
            child = crossover(parent1, parent2)

            # 4.3) mutate
            child = mutate(child, mutation_rate=mutation_rate)

            # 4.4) add child to new population
            new_population.append(child)

        # Refresh population
        population = new_population

        best = min(front, key=lambda x: (x[1][0], x[1][1]))
        print(f'[Gen {gen}.] Best cost: {best[1][0]:.2f} | Error: {best[1][1]:.2f}')

    return pareto.get_front(population, fitness_eval(population, workers))