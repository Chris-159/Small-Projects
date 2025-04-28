import polygon as poly
import core as algorithm


content = poly.content_get("test1.txt")

if content != None:
    polygon_points = poly.init(content["K"], content["points"], offset=poly.OFFSET)
    fig = poly.plot_init()
    
    best_candidate = algorithm.tabu_search(polygon_points, 
                          content["points"], 
                          display_func=poly.display, 
                          content=content,
                          show_each_step=False,
                          show_each_outcome=True)
    
    poly.display(best_candidate, content, stop_time=5.0)
    print("Done!")
else:
    print("No data was extracted from the file! It is possible, that you miswrote the filename.\n")
