#!/usr/bin/env python3
import os
from argparse import ArgumentParser


def scale_obj_file_in_place(file_path, scale_factor=1.0):
    with open(file_path, "r") as infile:
        lines = infile.readlines()

    with open(file_path, "w") as outfile:
        for line in lines:
            if line.startswith("v "):
                parts = line.split()
                x = float(parts[1]) * scale_factor
                y = float(parts[2]) * scale_factor
                z = float(parts[3]) * scale_factor
                outfile.write(f"v {x} {y} {z}\n")
            else:
                outfile.write(line)


def main(folder_path, scale_factor):
    for filename in os.listdir(folder_path):
        if filename.endswith(".obj"):
            file_path = os.path.join(folder_path, filename)
            scale_obj_file_in_place(file_path, scale_factor)


if __name__ == "__main__":
    parser = ArgumentParser(description="Scale .obj files.")
    parser.add_argument(
        "folder", type=str, help="Path to the folder containing .obj files."
    )
    parser.add_argument(
        "--scale", type=float, default=1.0, help="Scale factor. Default: 1.0"
    )
    args = parser.parse_args()
    main(args.folder, args.scale)
