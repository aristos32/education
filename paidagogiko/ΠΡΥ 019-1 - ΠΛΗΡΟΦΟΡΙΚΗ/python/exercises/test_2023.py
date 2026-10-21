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

            # odd numbers
            if num % 2 == 0:
                if num in listOdd:
                    listOdd.append(num)
            else:
                listEven.append(num)
                       

        print(listOdd)
        print(listEven)
       
       
    fileIn.close()
   

process_number("in.txt", "in2")