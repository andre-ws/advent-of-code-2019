import math

def getFuelByMass(x):
    return math.floor(x/3)-2

def main():
    input = open("input.txt", "r")
    sum = 0
    for line in input:
        sum += getFuelByMass(int(line))
    print(sum)

main()