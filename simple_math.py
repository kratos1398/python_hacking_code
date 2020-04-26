import argparse
# this is a program using argparse. 
parser = argparse.ArgumentParser(description= " This is to find the area of a rectangle")
parser.add_argument('-l', '--length', type = int,metavar = "", help = "The length of the rectangle")
parser.add_argument('-w', '--width', type = int,metavar = "", help = "The width of the rectangle")

arg = parser.parse_args()
if arg.length:
    length = arg.length
else:
    length = raw_input("Enter a length: ")
if arg.width:
    width = arg.width
else:
    width = raw_input("Enter a width: ")


def area(first,second):
    total = first * second
    return total

print area(int(length), int(width))