def dominates(x:tuple, y:tuple) -> bool:
    cost1, error1 = x
    cost2, error2 = y

    return (cost1 <= cost2 and error1 <= error2) and (cost1 < cost2 or error1 < error2)

def get_front(population:list[list[int]], fitnesses:list[tuple[float, float]]) -> list[list[int], tuple[float, float]]:
    pareto_front = []

    for i, fit_i in enumerate(fitnesses):
        dominated = False
        for j, fit_j in enumerate(fitnesses):
            if j != i and dominates(fit_j, fit_i):
                dominated = True
                break
        if not dominated:
            pareto_front.append((population[i], fit_i))

    return pareto_front