def cariNilaiMax(nilai):
    nilai_awal = nilai[0]
    max = nilai_awal
    for elemen in nilai:
        if elemen > max:
            max = elemen
    return max

def cariNilaiMin(nilai):
    nilai_awal = nilai[0]
    min = nilai_awal
    for elemen in nilai:
        if elemen < min:
            min = elemen
    return min

nilai = [2, 1, -8, 3, 2] #list
print(nilai)
print("Nilai Min =", cariNilaiMin(nilai))
print("Nilai Max =", cariNilaiMax(nilai))