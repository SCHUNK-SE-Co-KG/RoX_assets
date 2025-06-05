#!/usr/bin/env python3
import argparse
import xml.etree.ElementTree as ET


def main(file_path, scale_factor):
    tree = ET.parse(file_path)
    root = tree.getroot()

    for pose in root.iter("pose"):
        values = pose.text.split()
        if len(values) >= 3:
            x = float(values[0]) * scale_factor
            y = float(values[1]) * scale_factor
            z = float(values[2]) * scale_factor
            pose.text = f"{x} {y} {z} " + " ".join(values[3:])

    tree.write(file_path, xml_declaration=True, encoding="utf-8")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Scale <pose> x,y,z values in .sdf files."
    )
    parser.add_argument("file", type=str, help="The .sdf file to scale.")
    parser.add_argument(
        "--scale", type=float, default=1.0, help="Scale factor. Default: 1.0"
    )
    args = parser.parse_args()
    main(args.file, args.scale)
