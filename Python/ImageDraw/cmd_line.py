import sys
import argparse

import image_reader as img_read
import file_ops as fl

def cmd_get_and_process() -> int:
    # Get command line args
    arguments = sys.argv[1:]

    code = cmd_enum_args(enumerate(arguments))

    if code < 0:
        return code

    return 0

def cmd_enum_args() -> int:
    parser = argparse.ArgumentParser(description="A command line tool that converts a text defined image to a png image file.")

    parser.add_argument("--src", "-s", type=str, help="the path to the text file (necessary)",)
    parser.add_argument("--show", "-S", action="store_true", help="if specified the created image will be shown after conversion (not necessary)")
    parser.add_argument("--out", "-o", type=str, help="the path to the save directory (not necessary)")
    parser.add_argument("--name", "-n", type=str, help="the name of the output (PNG) image (not necessary)")

    args = parser.parse_args()

    show_out = False
    blanks, out = [], []
    rows, columns = 0, 0
    if args.src:
        out = fl.file_readTXT(args.src, blanks)

        if out is None:
            print("[TxtToPNG - ERROR] The path you specified does not exists!")
            return -1

        rows = len(out)
        columns = int(len(out[0]) / 3)
    else:
        print("[TxtToPNG - ERROR] No file path provided! To specify a path use the '--src' or '-s' flags.")
        return -2

    if args.show:
        show_out = True

    outcome = img_read.image_create((rows, columns), out, blanks, out_name=args.name, out_path=args.out, show_outcome=show_out)
    if outcome < 0:
        print(f"[TxtToPNG - ERROR] The png file can't be created! Error code: {outcome}")
        return -3

    print(f"\n[TxtToPNG] Png created with the size:: |width: {columns} height: {rows}|")
    return 0
