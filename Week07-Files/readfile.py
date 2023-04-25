FILENAME = "count.txt"

def readNumber():
    with open(FILENAME) as f:
        number = int(f.read())
        return number

# test it
num = readNumber()
print(num)

def writeNumber(number):
    with open(FILENAME, "wt") as f:
        #write takes a string so we need to convert
        f.write(str(number))

# test it
writeNumber(7)

num = readNumber()
num += 1
print(f"We have run this program {num} times.")
writeNumber(num)

