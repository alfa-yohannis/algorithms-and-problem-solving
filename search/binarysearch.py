def binary_search(nilai_dicari, daftar_nilai):
    index = -1
    index_awal = 0
    index_akhir = len(daftar_nilai) - 1
    while(index_awal <= index_akhir):
        index_tengah = int((index_awal + index_akhir) / 2)
        nilai_tengah = daftar_nilai[index_tengah]
        if nilai_tengah == nilai_dicari:
            index = index_tengah
            return index
        elif nilai_tengah < nilai_dicari:
            index_awal = index_tengah + 1
        elif nilai_tengah > nilai_dicari:
            index_akhir = index_tengah - 1 
    return index
    
daftar_nilai = [1, 4 ,10, 23, 28, 31, 33, 43, 48] 
#daftar_nilai = [48, 43, 33, 31, 28, 23, 10, 4, 1] 
nilai_dicari = 1
index = binary_search(nilai_dicari, daftar_nilai)
print("Index dari nilai", nilai_dicari, "adalah", index)
