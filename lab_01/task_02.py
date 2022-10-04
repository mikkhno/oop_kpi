import argparse
import math
import operator

parser = argparse.ArgumentParser(description="Calculating universal math operations")
parser.add_argument('operators', type=str)
parser.add_argument('num1', type=float)
parser.add_argument('num2', type=float)
args = parser.parse_args()

performing = getattr(math, args.operators, None)
if performing:
    performing_res = getattr(math, args.operators)
else:
    performing_res = getattr(operator, args.operators)

print(performing_res(args.num1, args.num2))

