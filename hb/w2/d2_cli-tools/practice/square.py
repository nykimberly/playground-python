import argparse
parser = argparse.ArgumentParser()
parser.add_argument("integer", metavar='N', help="display a square of a given number",
                    type=int)
args = parser.parse_args()
print(args.integer**2)
