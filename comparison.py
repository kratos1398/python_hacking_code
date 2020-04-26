import argparse

parser = argparse.ArgumentParser(description="The length comparison of two strings.")
parser.add_argument("-f","--first",metavar="",help="First string")
parser.add_argument("-s","--second",metavar="",help="Second string")
args = parser.parse_args()

if args.first:
    first = args.first
else:
    first = input("Enter first string: ")
if args.second:
    second = args.second
else:
    second = input("Enter second string: ")

def Comparison(str1, str2):
    if len(str1) > len(str2):
        return "first"
    elif len(str2) > len(str1):
        return "second"
    else:
        return "same"

function = Comparison(first, second)
if function == "first":
    print("{} of length {}, is a bigger string than the second.".format(first, len(first))) 
elif function == "second":
    print("{} of length {}, is a bigger string than the first".format(second, len(second)))
else:
    print("They are both the same") 
