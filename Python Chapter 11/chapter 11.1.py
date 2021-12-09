from datetime import*

def diffDate(x):
    try:
        sekarang = datetime.date(datetime.now())
        #inputan x di split dulu -
        #agar bisa dipecah tahun bulan dan tanggalnya
        x = x.split('-')
        x = date(int(x[0]),int(x[1]),int(x[2]))
        result = x - sekarang
        result = result.days
    except ValueError:
        result = False #jika date yang dimasukkan salah
    return result

diffDate('2021-12-09')