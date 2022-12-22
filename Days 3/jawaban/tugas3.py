# DAYS3

print("DAY3_LV1")
umur = 18
tinggi = 163,5

print(20*"=" + "\n") 
print("SEGITIGA")
alas = int(input("Masukan alas: ",))
tinggi = int(input("Masukan tinggi: ",))
luas_segitigas = 0.5 * alas * tinggi
print("Luas segitiga:", luas_segitigas) 
print(20*"=" + "\n") 
a = int(input("Masukan sisi a: ",))
b = int(input("Masukan sisi b: ",))
c = int(input("Masukan sisi c: ",))
keliling_segitiga = a + b + c
print("Keliling segitiga: ", keliling_segitiga) 

print(20*"=" + "\n") 
print("PERSEGI PANJANG")
panjang = int(input("Masukan panjang: ",))
lebar = int(input("Masukan lebar: ",))
luas_persegi_panjang = panjang*lebar
keliling_persegi_panjang = 2 * (panjang + lebar)
print("Luas persegi panjang: ", luas_persegi_panjang)
print("Keliling persegi panjang: ", keliling_persegi_panjang)

print(20*"=" + "\n") 
print("LINGKARAN")
rad = int(input("Masukan jari-jari: ",))
phi = 3.14
luas_lingkaran = phi * rad * rad
keliling_lingkaran = 2 * phi * rad
print("Luas lingkaran: ", luas_lingkaran)
print("Keliling lingkaran: ", keliling_lingkaran) 


