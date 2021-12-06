file = open('datacp10.txt', 'r')

ganjil = 0
genap = 0 

for i in file :
    teks = int(i)
    if teks % 2 == 0 :
        genap += 1
    else :
        ganjil += 1

print(f'Banyak bilangan genap   : {genap}')
print (f'Banyak bilangan ganjil  : {ganjil}')

file.close()

