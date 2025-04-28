import random
import copy
import polygon as poly

import numpy as np

# The temperature function
def temperature_schedule(iter, max_iter, start_temp=100.0, end_temp=0.1):
    return start_temp * ((end_temp / start_temp) ** (iter / max_iter))

def simulated_annealing(polygon_points, data_points, max_iter=100, display_func=None, content=None):
    current = polygon_points
    best = polygon_points
    best_area = poly.area(current)

    for iter in range(max_iter):
        candidate = hill_climber_random_step(current, data_points)

        if candidate is None:
            continue

        area_current = poly.area(current)
        area_candidate = poly.area(candidate)

        dt = area_candidate - area_current
        T = temperature_schedule(iter, max_iter)

        if dt < 0:
            current = candidate
            if area_candidate < best_area:
                best = candidate
                best_area = area_candidate
        else:
            acceptance_ = np.exp(-dt / T)
            if random.random() < acceptance_:
                current = candidate

            if display_func and content:
                display_func(current, content)

    return best

def hill_climber_random_step(polygon_points, data_points) -> list | None:
    current_polygon = copy.deepcopy(polygon_points)
    i = random.randint(0, len(current_polygon) - 1)

    direction = poly.DIRECTIONS[random.randint(0, 3)]
    candidate_polygon = copy.deepcopy(current_polygon)
    candidate_polygon[i][0] += direction[0]
    candidate_polygon[i][1] += direction[1]

    if all(poly.is_point_inside(candidate_polygon, point) for point in data_points):
        return candidate_polygon

    return None