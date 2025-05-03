def content_get(file_name:str) -> dict:
    if file_name is None:
       return None
    
    workers = []
    n_workers = int(0)

    try:
        with open(file_name, 'r') as file:
            content_raw = file.readlines()
            n_workers = int(content_raw[0].strip())

            for line in content_raw[1:n_workers+1]:
                wage, error_rate = map(float, line.strip().split())
                workers.append((wage, error_rate))
    except:
        return None

    return {
        "N": n_workers,
        "workers": workers
        }