import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-o", "--output", help="Show output message")
args = parser.parse_args()

if args.output:
    print("Output: ", args.output)
