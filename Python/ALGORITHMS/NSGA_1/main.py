import basics as bs
import genetic

content = bs.content_get("workers1.txt")

if content != None:
    final_front_ = genetic.genetic_algorithm(content, population_size=10, generations=10)

    print("\nFinal Pareto Front:")
    for ind, (cost, error) in final_front_:
        print(f'{ind} -> Cost: {cost:.2f} | Error: {error:.2f}')
else:
    print("No data was extracted from the file! It is possible, that you miswrote the filename.\n")
