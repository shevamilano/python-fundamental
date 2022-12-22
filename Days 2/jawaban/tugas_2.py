# "Hari ke-2: Fundamental Python"

print("DAY2_LVL1")
nama = "Sheva Haya Milano"
jurusan = "Ilmu Komputer"
angkatan = 22
umur = 18
asal_daerah = "Jakarta"
money_amount = 100000000
is_mahasiswa = True
is_alien = False 

print(nama) 
print(jurusan)
print(angkatan)
print(umur)
print(asal_daerah)
print(money_amount)
print(is_mahasiswa)
print(is_alien)

print("DAY2_LVL2")
# 1
print(type(nama))
print(type(jurusan))
print(type(angkatan))
print(type(umur))
print(type(asal_daerah))
print(type(money_amount))
print(type(is_mahasiswa))
print(type(is_alien))

# 2
print(len(nama))

# 3
num_one = 5
num_two = 4
total = num_one + num_two
diff = num_one - num_two
product = num_one * num_two
division = num_one / num_two 
remainder = num_one % num_two 
exp = num_one ^ num_two
floor_division = num_one ** num_two

print("1. Penjumlahan num_one dan num_two: ", total)
print("2. Pengurangan num_one dan num_two: ", diff)
print("3. Perkalian num_one dan num_two: ", product)
print("4. Pembagian num_one dan num_two: ", division)
print("5. Modulus num_one dan num_two: ", remainder)
print("6. Eksponensial num_one dan num_two: ", exp)
print("7. Floor divison num_one dan num_two: ", floor_division)
print("")

# 4
print(input(nama))
print(input(umur))
print(input(asal_daerah))

# 5
rad = int(input("Masukan nilai jari-jari: ",))
phi = 3.14
area_of_circle = phi * rad * rad
circum_of_circle = 2 * phi * rad
print("Luas lingkaran: ", area_of_circle)
print("Keliling lingkarang: ", circum_of_circle)

# 6
help('keyword')
