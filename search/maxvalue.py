#nilai = {4, 6, 7, 1, 4} #set
nilai = [2, 1, 3, 2] #list
print(nilai)

nilai_awal = nilai[0]
max = nilai_awal
for elemen in nilai:
    if elemen > max:
        max = elemen

print("Nilai Max =", max)