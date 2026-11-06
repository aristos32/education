# Άσκηση 3: countlines αντικαθιστά τις τέσσερις επαναλήψεις

def countlines(filename):
    f = open(filename)
    count = 0
    for line in f:
        count = count + 1
    f.close()
    return count


print("File input3one.txt has", countlines("input3one.txt"), "lines")
print("File input3two.txt has", countlines("input3two.txt"), "lines")
print("File input3three.txt has", countlines("input3three.txt"), "lines")
print("File input3four.txt has", countlines("input3four.txt"), "lines")
