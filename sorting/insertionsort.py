daftar_nilai_awal = [9, 9, 9, 5,5, 3, 87, 3, 1]

def insertion_sort(daftar_nilai):
    for i in range(1, len(daftar_nilai)):
        nilai_yang_dicek = daftar_nilai[i]
        index_sebelum = i - 1
        nilai_sebelum = daftar_nilai[index_sebelum]
        index_sisip = i
        #cek posisi index untuk disisip
        while(nilai_sebelum > nilai_yang_dicek and index_sebelum >= 0):
            nilai_sebelum = daftar_nilai[index_sebelum]
            index_sisip = index_sebelum
            index_sebelum = index_sebelum - 1
        # geser
        for pos in range(i, index_sisip, -1):
            daftar_nilai[pos] = daftar_nilai[pos - 1]
        #sisipkan
        daftar_nilai[index_sisip] = nilai_yang_dicek

    return daftar_nilai

print("Awal:",daftar_nilai_awal)
daftar_nilai_akhir = insertion_sort(daftar_nilai_awal)
print("Akhir:",daftar_nilai_akhir)


