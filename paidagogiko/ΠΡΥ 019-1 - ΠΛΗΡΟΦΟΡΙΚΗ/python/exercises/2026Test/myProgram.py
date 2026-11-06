# function declarations
def decompress(compressed):
    
    result = ''
    index = 0
    decompress_times = '0'
    
    # parse string
    for char in compressed:
        
        if char.isdigit():
            
            # concatenate to support more than one digit number
            decompress_times = decompress_times + char
            
        else:

            # default repetitions for uncompressed chars
            repetitions = 1

            # if digit(s) exist, use that as repetition
            if int(decompress_times) != 0:
                repetitions = int(decompress_times)

            # add characters based on repetitions
            for i in range(0, repetitions):
                result = result + char

            # set for next repetition
            decompress_times = '0'
    
    return result

# sample.txt

# input
filename = input("Give a filename:")

#open for read
inputFile = open(filename, "r")

#get content
compressed = inputFile.read()

#find initial text
decompressed = decompress(compressed)

#open for write
outputFile = open("decompressed.txt", "w")

# store decompressed
outputFile.write(decompressed)
outputFile.close()

#calculate expansion ratio
expansionRatio = (len(decompressed) / len(compressed) -1 ) * 100
expansionRatio = round(expansionRatio, 2)

#print results
print(f"Compressed text: {compressed}")
print(f"Decompressed text: {decompressed}")
print(f"Expansion ratio: {expansionRatio}%")


