file = open("file.txt", "a+")

while True:
    nim = input('\nMasukkan NIM           :')
    nama = input('Masukkan Nama Mhs      :')
    alamat = input('Masukkan Alamat        :')
    file.write((f'{nim}|{nama}|{alamat}\n'));
    file.seek(0,0)
    ulangi = input('\nUlangi input lagi [y/n] :')
    if ulangi.lower() not in 'y': break

print(f'\n{file.read()}')

file.close()