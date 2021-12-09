from datetime import *

def terlambat(x):
    now = datetime.date(datetime.now())
    x = datetime.strptime(x, '%Y-%m-%d').date()
    return abs((now - x).days)

myFile = open('dataPeminjam.txt', 'r')
isiFile = myFile.read().splitlines()

cariKode = input('Masukkan Kode Member     : ')
print()
for i in range(len(isiFile)):
    if cariKode in isiFile[i]:
        status = 'Ada'
        data = isiFile[i].split('|')
        break
    else:
        status = 'Tidak ada'
        continue

if status == 'Ada':
    telat = terlambat(data[3])

    if (telat <= 7):
        telatKembali = '0 Hari'
        denda = 'Rp. 0'
    elif (telat > 7):
        telat1 = terlambat(data[4])
        telatKembali = str(telat1) + ' Hari'
        denda = 'Rp. ' + str(telat1*2000)

    print('Data Peminjaman Buku')
    print('Kode Member              :', data[0])
    print('Nama Member              :', data[1])
    print('Judul Buku               :', data[2])
    print('Tanggal Mulai Peminjaman :', data[3])
    print('Tanggal Maks Peminjaman  :', data[4])
    print('Tanggal Pengembalian     :', datetime.date(datetime.now()))
    print('Terlambat                :', telatKembali)
    print('Denda                    :', denda)
    
else:
    print('Maaf kode member yang anda masukkan tidak ada')

myFile.close()