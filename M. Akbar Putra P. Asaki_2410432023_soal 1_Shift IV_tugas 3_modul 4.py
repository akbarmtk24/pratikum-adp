b = int(input("masukan nilai baris : "))
k = int(input("masukan nilai kolom : "))

for i in range (b):
    print()
    for j in range (k):
        if (i + j) % 2 == 0 :
            print (" X ",end="")
        else :
            print (" O ",end="")


