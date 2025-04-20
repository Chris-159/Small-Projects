import polygon as poly
import core as algorithm


content = poly.content_get("test1.txt")

if content != None:
    polygon_points = poly.init(content["K"], content["points"], offset=poly.OFFSET)
    fig = poly.plot_init()
    
    for _ in range(poly.MAX_ITER):
        polygon_optimized = algorithm.hill_climber_steepest_ascent(polygon_points, content["points"], offset=poly.OFFSET)
        poly.display(polygon_optimized, content)
        polygon_points = polygon_optimized
        
else:
    print("No data was extracted from the file! It is possible, that you miswrote the filename.\n")
