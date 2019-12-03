import math

def getFuelByMass(x):
    return math.floor(x/3)-2

def getTotalFuelByMass(x):
    fuel = getFuelByMass(x)
    if (fuel > 0):
        return fuel + getTotalFuelByMass(fuel)
    return 0;

def main():
    input = open("input.txt", "r")
    sum = 0
    for line in input:
        sum += getTotalFuelByMass(int(line))
    print(sum)

main()