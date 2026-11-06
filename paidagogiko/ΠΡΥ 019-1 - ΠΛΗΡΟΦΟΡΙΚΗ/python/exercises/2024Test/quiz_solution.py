def find_greater_than(inputFile, number):
    result = 0

    fileIn = open(inputFile, "r")
    
    #parse line by line
    for line in fileIn:
        lista = line.split()

        #parse word by word
        for word in lista:

            # is number
            if word.isdigit():                

                # compare with number
                if int(word) > number:
                    result = result + 1

    return result


# input numbers
inputFile = input("Enter file name to read:")
number = int(input("Enter number to check:"))

result = find_greater_than(inputFile, number)

print(f"The count of numbers in file {inputFile} that are greater than {number} are {result}")
