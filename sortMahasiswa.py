import random
from dataMahasiswa import data
from fungsiMahasiswa import show_data, presensi_dummy, acak_data

data = data.copy()
presensi_dummy(data)
acak_data(data)



def sort_by(data: list=data, index: str="nim",rev = False):
    maps = {
        "nim":0,
        "nama":1,
        "presensi":2,
    }
    
    # Kerjakan disini
    col = maps[index]
    n = len(data)

    for i in range(n - 1):
        for j in range(n - 1 - i):
            kiri = data[j][col]
            kanan = data[j + 1][col]

            if index == "presensi":
               kiri = int(kiri)
               kanan = int(kanan)

            if not rev:
               if kiri > kanan:
                  data[j], data[j + 1] = data[j + 1], data[j]
            else:
                if kiri < kanan:
                    data[j], data[j + 1] = data[j + 1], data[j]
            
    # Jangan Dihapus
    show_data(data)

sort_by(data, "presensi" )
sort_by(data, "nim", rev=True)
sort_by(data, "nama")


    
