def process_number(file_inp, file_out):
    fileIn = open(file_inp, "r")
    fileOut = open(file_out, "w")

    listOdd = []
    listEven = []    

    # loop through file
    for line in fileIn:
        lista = line.split()

        # loop through list
        for arithmos in lista:
            num = int(arithmos)

            # only unique 
            if num not in listOdd:
                
                # odd numbers
                if num % 2 == 0:                
                    listEven.append(num)
                else:
                    listOdd.append(num)
                       
  
    # sort odd
    listOdd.sort()

    # extend content of list at end of first
    # append will insert second list as one element of first list
    listOdd.extend(listEven)

    for num in listOdd:
        fileOut.write(str(num) + ' ')
   
    fileIn.close()
    fileOut.close()

process_number("in.txt", "output.txt")
