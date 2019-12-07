def isValid(number):
    digits = str(number)
    matchingCount = 1
    hasPair = False
    for i in range(len(digits) - 1):
        digit = digits[i+1]
        previousDigit = digits[i]
        if (int(digit) < int(previousDigit)):
            return False
        if (digit == previousDigit):
            matchingCount += 1
        elif (matchingCount == 2):
            hasPair = True
        elif (matchingCount > 1):
            matchingCount = 1
    return hasPair or matchingCount == 2

assert(isValid(112233))
assert(isValid(111122))
assert(not isValid(123444))
assert(not isValid(111123))

def main():
    input = open("input.txt", "r").read()
    min, max = input.split('-')
    count = 0
    for i in range(int(min), int(max)):
        if (isValid(i)):
            count += 1
    print(count)

main()
