import math

def calc_euclidean_distance(point1:list[int], point2:list[int]) -> float:
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

def calc_path_length(path:list[int], points:list[list[int]]) -> float:
    path_length = 0.0

    for i in range(len(path) - 1):
        city_from = points[path[i]]
        city_to = points[path[i + 1]]
        path_length += calc_euclidean_distance(city_from, city_to)

    return path_length