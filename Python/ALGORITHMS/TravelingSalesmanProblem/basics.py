def content_get(file_name:str) -> dict:
    if file_name is None:
       return None
    
    try:
        with open(file_name, 'r') as file:
            content_raw = file.readlines()
    except:
        return None
    
    # N - how many cities are there
    N = int(content_raw[0])

    points = []
    for line in content_raw[1:]:
        line_conv = list(map(int, line.split()))
        points.append(line_conv)

    return {
        "N": N,
        "points": points
        }