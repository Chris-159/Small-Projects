import polygon as poly
import core as algorithm

content = poly.content_get("test1.txt")

if content != None:
    polygon_points = poly.init(content["K"], content["points"], offset=poly.OFFSET)
    fig = poly.plot_init()
    
    algorithm.simulated_annealing(polygon_points, content["points"],
                                  max_iter=500,
                                  display_func=poly.display,
                                  content=content)
        
else:
    print("No data was extracted from the file! It is possible, that you miswrote the filename.\n")
