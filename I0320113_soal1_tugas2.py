import math

# menghitung luas persegi panjang
panjang = 24
lebar = 10

luas_persegi_panjang = panjang*lebar

print("1. Menghitung luas persegi panjang")
print("Panjang :", panjang)
print("Lebar : ", lebar)
print("Luas : ", luas_persegi_panjang)


# menghitung luas lingkaran
r = float(40)

luas_lingkaran = 3.14 * (r ** 2)

luas_int = int(luas_lingkaran)

print("2. Menghitung Luas Lingkaran")
print("Jari-jari : ", r)
print("Luas lingkaran : ", luas_int)

# Menghitung Luas Permukaan Kubus
sisi = 9

luas_kubus = 6 * (sisi ** 2)

print("3. Menghitung Luas Permukaan Kubus")
print("Panjang sisi : ", sisi)
print("Luas Permukaan Kubus : ", luas_kubus)


# Konversi Suhu Celsius ke Fahrenheit
C = float(45)

F = (9/5)* C + 32

print("4. Konversi Suhu Celcius ke Fahrenheit")
print("Celsius : ", C)
print("Fahrenheit : ", F)

# Konversi Suhu Reamur ke Kelvi
R = float(56)

K = (5/4)* R + 273

print("5. Konversi Suhu Reamur ke Kelvin")
print("Reamur : ", R)
print("Kelvin : ", K)