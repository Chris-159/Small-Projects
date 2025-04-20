import random
import copy
import polygon as poly

def hill_climber_steepest_ascent(polygon_points, data_points, max_iter=100, offset=0):
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