daftar_nilai_awal = [9, 9, 9, 5,5, 3, 87, 3, 1]

def selection_sort(daftar_nilai):
    for i in range(0, len(daftar_nilai)):
        #cari nilai minimum
        nilai_awal = daftar_nilai[i]
        index_min = i
        nilai_min = nilai_awal
        for index_cari_min in range(i, len(daftar_nilai)):
            nilai_cari_min = daftar_nilai[index_cari_min]
            if nilai_cari_min < nilai_min:
                index_min = index_cari_min
                nilai_min = nilai_cari_min
        # tukar nilai
        # x, y = y, x
        daftar_nilai[i], daftar_nilai[index_min] = \
        daftar_nilai[index_min] ,daftar_nilai[i]    

    return daftar_nilai

print("Awal:",daftar_nilai_awal)
daftar_nilai_akhir = selection_sort(daftar_nilai_awal)
print("Akhir:",daftar_nilai_akhir)


