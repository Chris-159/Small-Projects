def file_readTXT(path: str = None, blank_px: list = None) -> list | None:
    if blank_px == None:
        return None

    try:
        with open(path, 'r') as file:
            # read all data
            lines = file.readlines()

            values_ = []
            line_index = 0
            for line in lines:
                index = 0
                # Split each string into separate element, trim white space
                str_nums = line.strip().split()

                # Search for blank pixels, read 3 values (RGB) and determin if it is flagged
                for i in range(0, len(str_nums), 3):
                    batch = str_nums[i:i+3]

                    contains = False
                    saved = False
                    # Search for blank pixel flag
                    for j in range(len(batch)):
                        if batch[j] == "T" or batch[j] == "t":  # If it is flagged
                            str_nums[i + j] = "0"
                            contains = True
                        if contains and not saved:              # Be aware of multiple flagging
                            blank_px.append([line_index, index])
                            saved = True
                            
                    index += 1
                line_index += 1

                # Convert each string element into integer
                numbers_ = [int(value) for value in str_nums]
                # Append the converted numbers as new rows
                values_.append(numbers_)

            return values_
        
    except Exception as ex:
        print(f"Something went wrong!\nError: {ex}")

    return None
