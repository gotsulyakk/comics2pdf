import argparse
from comics_to_pdf import ComicsToPDF


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-s", "--source", help="source comics file")
    parser.add_argument("-d", "--destination", help="destination pdf path")
    args = parser.parse_args()

    converter = ComicsToPDF(args.source, args.destination)
    converter.convert_comics()

    print(f"Converted successfully to {args.destination}")


if __name__ == "__main__":
    main()
