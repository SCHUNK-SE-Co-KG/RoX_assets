#!/usr/bin/env python3
from argparse import ArgumentParser

import glob
import os

# Method         | Compression Level | Compatibility     | Speed
# -------------- | ----------------- | ------------------| -------------
# ZIP_STORED     | None              | Universal         | Fastest
# ZIP_DEFLATED   | Medium            | Universal         | Fast
# ZIP_BZIP2      | High              | Limited support   | Slower
# ZIP_LZMA       | Highest           | Limited support   | Slowest
from zipfile import ZipFile, ZIP_DEFLATED

# Notes:
# - ZIP_DEFLATED is the best balance of compression and compatibility.
# - ZIP_LZMA gives the smallest file size but may not open on older systems.


target = "../assets/egk_25.zip"


def main(sdf_file: str, cad_folder: str) -> None:
    with ZipFile(target, "w", compression=ZIP_DEFLATED) as f:

        # .sdf
        f.write(sdf_file, arcname=os.path.basename(sdf_file))

        # .obj
        obj_files = glob.glob(os.path.join(cad_folder, "*.obj"))
        for file in obj_files:
            f.write(file, arcname=os.path.basename(file))

        # .mtl
        mat_files = glob.glob(os.path.join(cad_folder, "*.mtl"))
        for file in mat_files:
            f.write(file, arcname=os.path.basename(file))


if __name__ == "__main__":
    parser = ArgumentParser(description="Create a RoX asset.")
    parser.add_argument("sdf_file", type=str, help="Path to the .sdf file.")
    parser.add_argument(
        "obj_folder", type=str, help="Path to the folder containing .obj files."
    )
    args = parser.parse_args()
    main(args.sdf_file, args.obj_folder)
