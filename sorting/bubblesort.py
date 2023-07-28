daftar_nilai_awal = [9, 9, 9, 5,5, 3, 87, 3, 1]

def bubble_sort(daftar_nilai):
    for index1 in range(0, len(daftar_nilai) - 1):
        for index2 in range(0, len(daftar_nilai) -1 - index1):
            if daftar_nilai[index2] > daftar_nilai[index2+1]:
                daftar_nilai[index2] , daftar_nilai[index2+1] = \
                daftar_nilai[index2 + 1] , daftar_nilai[index2]
    return daftar_nilai

print("Awal:",daftar_nilai_awal)
daftar_nilai_akhir = bubble_sort(daftar_nilai_awal)
print("Akhir:",daftar_nilai_akhir)


