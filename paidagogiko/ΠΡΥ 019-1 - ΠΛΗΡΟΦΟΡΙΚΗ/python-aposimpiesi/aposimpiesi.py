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

# input
compressed = input("Give a compressed string: ")

decompressed = decompress(compressed)



# present result
print(decompressed)
