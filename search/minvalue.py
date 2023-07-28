#nilai = {4, 6, 7, 1, 4} #set
nilai = [2, 1, -8, 3, 2] #list
print(nilai)

nilai_awal = nilai[0]
min = nilai_awal
for elemen in nilai:
    if elemen < min:
        min = elemen

print("Nilai Min =", min)