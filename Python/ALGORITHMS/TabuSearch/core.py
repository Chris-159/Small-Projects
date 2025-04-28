import random
import copy
import polygon as poly

import numpy as np

def is_similar_to_tabu(candidate, tabu_list, tolerance=1.0) -> bool:
    for old in tabu_list:
        distances = [np.linalg.norm(np.array(p1) - np.array(p2)) for p1, p2 in zip(candidate, old)]
        if max(distances) < tolerance:
            return True
        
    return False

def tabu_search(polygon_points, data_points, max_iter=10, iter_per_run=100, display_func=None, content=None, show_each_step=False, show_each_outcome=False):
    tabu_list = []
    best_candidate = None
    best_area = float('inf')

    for _ in range(max_iter):
        current = polygon_points
        for _ in range(iter_per_run):
            candidate = hill_climber_steepest_ascent(current, data_points)

            if is_similar_to_tabu(candidate, tabu_list):
                break
            
            current = candidate

            if show_each_step and display_func and content:
                display_func(current, content)

        area = poly.area(current)
        if area < best_area:
            best_area = area
            best_candidate = current

        tabu_list.append(current)

        if show_each_outcome and display_func and content:
            display_func(best_candidate, content)

    return best_candidate

def hill_climber_steepest_ascent(polygon_points, data_points):
    current_polygon = polygon_points
    polygon_length = len(polygon_points)

    #for _ in range(max_iter):
    best_polygon = current_polygon
    best_area = poly.area(best_polygon)

    for i in range(polygon_length):
        ### THE LOGIC TO DETERMINE A NEW POINT ##
        # generate direction offset
        random_direction = poly.DIRECTIONS[random.randint(0, 3)]

        # create a candidate for further validations
        polygon_candidate = copy.deepcopy(best_polygon)
        # apply direction offset
        polygon_candidate[i][0] += random_direction[0]
        polygon_candidate[i][1] += random_direction[1]

        #if polygon_candidate[i][0] < offset or polygon_candidate[i][1] < offset:
        #    continue

        # if all points are inside the candidate polygon
        if all(poly.is_point_inside(polygon_candidate, point) for point in data_points):
            # calculate the area of the candidate
            area_candidate = poly.area(polygon_candidate)
            
            # if the area is better than the last on, 
            # change the current polygon properties to the candidate
            if area_candidate < best_area:
                best_polygon = polygon_candidate
                best_area = area_candidate
    
    # if there is a change, switch properties
    if best_polygon != current_polygon:
        current_polygon = best_polygon
    #else:
    #    break
    
    #[[x + offset, y + offset] for x, y in current_polygon]
    return current_polygon