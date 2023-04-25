def writeNumber(number):
    with open(FILENAME, "wt") as f:
 # write takes a string so we need to convert
        f.write(str(number))
# test it
writeNumber(3)
