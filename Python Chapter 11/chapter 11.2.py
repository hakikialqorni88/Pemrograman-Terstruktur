from datetime import *

myFile = open('dataPeminjam.txt', 'w')

while True:
    kodeMember = input('Masukkan Kode Member :')
    namaMember = input('Masukkan Nama Member :')
    judulBuku  = input('Masukkan Judul Buku  :')
    
    tglPinjam = datetime.date(datetime.now())
    tglKembali = tglPinjam + timedelta(days = 7)
    myFile.write('{0}|{1}|{2}|{3}|{4}\n'.format(kodeMember, namaMember, judulBuku, tglPinjam, tglKembali))

    print()
    ans = input('Ulangi lagi (y/n)    : ')
    print()
    if ans in ('N', 'n'):
        break

myFile.close()