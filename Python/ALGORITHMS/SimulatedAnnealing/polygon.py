import math
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

DIRECTIONS = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1]
]

OFFSET = int(5)
MAX_ITER = int(100)

def content_get(file_name:str) -> dict:
    if file_name is None:
       return None
    
    try:
        with open(file_name, 'r') as file:
            content_raw = file.readlines()
    except:
        return None
    
    # N - how many points are there
    # K - how many points the polygon will have
    N, K = list(map(int, content_raw[0].split()))

    points = []
    for line in content_raw[1:]:
        line_conv = list(map(int, line.split()))
        points.append(line_conv)

    return {
        "N": N,
        "K": K,
        "points": points
        }

def init(K:int, points:list[list[int]], offset:int = 0) -> list:
    sum_x = sum(point[0] for point in points)
    sum_y = sum(point[1] for point in points)
    points_length = len(points)

    center_x = round(sum_x / points_length)
    center_y = round(sum_y / points_length)

    radius = max(
        math.hypot(point[0] - center_x, point[1] - center_y)
        for point in points
    ) + offset

    polygon_ = []
    for i in range(K):
        angle = (2 * math.pi * i) / K
        x = center_x + radius * math.cos(angle)
        y = center_y + radius * math.sin(angle)
        polygon_.append([x, y])

    return polygon_

def is_point_inside(polygon_points:list[list[int]], data_point:list[int]) -> bool:
    incision_count = 0
    poly_length = len(polygon_points)

    for i in range(poly_length):
        point1 = polygon_points[i]
        point2 = polygon_points[(i + 1) % poly_length]

        if(data_point[1] > min(point1[1], point2[1]) and
           data_point[1] <= max(point1[1], point2[1]) and
           point1[1] != point2[1]):
            
            slope = (point2[0] - point1[0]) / (point2[1] - point1[1])
            incision_x = slope * (data_point[1] - point1[1]) + point1[0]

            if data_point[0] < incision_x:
                incision_count += 1

    return (incision_count % 2 == 1)

# Shoelace algorithm
def area(polygon_points:list[list[int]]) -> float:
    num_of_vertices = len(polygon_points)
    sum1, sum2 = 0, 0

    for i in range(num_of_vertices):
        x1, y1 = polygon_points[i]
        x2, y2 = polygon_points[(i + 1) % num_of_vertices]
        sum1 += x1 * y2
        sum2 += y1 * x2

    sum1 += polygon_points[num_of_vertices-1][0] * polygon_points[0][1]
    sum2 += polygon_points[0][0] * polygon_points[num_of_vertices-1][1]

    area = abs(sum1 - sum2) / 2
    return area

def plot_init():
    matplotlib.use("TkAgg")  # set backend for the plot (tkinter)
    plt.ion()                # interactive mode
    fig = plt.figure()

    return fig

def display(polygon_points:list[list[int]], content:dict, stop_time:float=0.5):
    xpointsPoly_raw = list(point[0] for point in polygon_points)
    ypointsPoly_raw = list(point[1] for point in polygon_points)
    xpointsCont_raw = list(point[0] for point in content["points"])
    ypointsCont_raw = list(point[1] for point in content["points"])

    xpointsPoly = np.array(xpointsPoly_raw)
    ypointsPoly = np.array(ypointsPoly_raw)
    xpointsCont = np.array(xpointsCont_raw)
    ypointsCont = np.array(ypointsCont_raw)

    #polygon_arr = np.array(polygon_points)
    #data_arr = np.array(content["points"])

    plt.clf() # clear the plot

    plt.plot(xpointsPoly, ypointsPoly, 'bs')
    plt.plot(xpointsCont, ypointsCont, 'ro')
    plt.legend(["Polygon border", "Data points"])
    plt.plot(np.append(xpointsPoly, [xpointsPoly[0]]), np.append(ypointsPoly, [ypointsPoly[0]]))

    for idx, point in enumerate(polygon_points):
        plt.text(point[0], point[1], str(idx), fontsize=9, color='blue')

    plt.pause(stop_time)