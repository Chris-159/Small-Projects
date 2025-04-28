import basics as bs
import genetic

content = bs.content_get("cities1.txt")

if content != None:
    points = content['points']
    best_length, best_path = genetic.genetic_algorithm(content)

    print(f'\nBest length: {best_length} | Best path: {best_path}\n')
else:
    print("No data was extracted from the file! It is possible, that you miswrote the filename.\n")
