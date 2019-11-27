import sys
from statistics import mean


def main():
    assert len(sys.argv) > 1, "No input file path specified."
    input_file_path = sys.argv[1]
    print(f"Processing input file: {input_file_path}")

    with open(input_file_path, "r") as f:
        for inputs in f:
            inputs = inputs.strip("\n")
            inputs_ting = inputs.split(",")
            giraffe = []
            for x in inputs_ting:
                giraffe.append(float(x))
                zebra = mean(giraffe)
            print(f"{zebra}")


if __name__ == "__main__":
    main()
