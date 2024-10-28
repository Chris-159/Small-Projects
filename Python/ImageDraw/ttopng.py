# import image_reader as img_read
# import file_ops as fl
import cmd_line as cmd_ln

if __name__ == "__main__":
    code = cmd_ln.cmd_enum_args()
    print(f"Code: {code}")
    # blanks = []
    # out = fl.file_readTXT("input.txt", blanks)
    # rows = len(out)
    # columns = int(len(out[0]) / 3)

    # print(blanks, end="\n\n")
    # print(f"Rows: {rows} | Cols: {columns}")

    # outcome = img_read.image_create((rows, columns), out, blanks, True)
    # print(f"Outcome code: {outcome}")

    # print("Values: ")
    # for num in out:
    #     print(f"{num}", end=" ")

    # print()
