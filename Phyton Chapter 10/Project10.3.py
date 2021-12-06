file = open("file.txt", "r")
readFile = file.readlines()
dataMhs = []

for i in range(len(readFile)):
    data = readFile[i].rstrip("\n")
    pecahData = data.split("|")
    dataDict = {'nim':pecahData[0], 'nama':pecahData[1], 'alamat':pecahData[2]}
    dataMhs.append(dataDict)

print(f'dataMhs = {dataMhs}')
file.close()