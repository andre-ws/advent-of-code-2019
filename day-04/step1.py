def isValid(number):
    digits = str(number)
    hasPair = False
    for i in range(len(digits) - 1):
        digit = digits[i+1]
        previousDigit = digits[i]
        hasPair = hasPair or digit == previousDigit
        if (int(digit) < int(previousDigit)):
            return False
    return hasPair

def main():
    input = open("input.txt", "r").read()
    min, max = input.split('-')
    count = 0
    for i in range(int(min), int(max)):
        if (isValid(i)):
            count += 1
    print(count)

main()
