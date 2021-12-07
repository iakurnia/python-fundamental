# 1.Cetak String
# untuk cetak string di rekomendasikan pakai single quote
# SEQUENTIAL = Eksekusinya Berurutan
print("---" * 10)
print('#1.Cetak String')
print("---" * 10)
print("Hello World")
nama = 'Ia Kurnia'
print('Nama Saya :', nama)
print("Ini  project pertama pyhton saya")
print("---" * 10)
print("\n")

# 2.Percabangan
print("---" * 10)
print('#2.Percabangan')
print("---" * 10)
print('#2.Percabangan 1 pilihan')
saya_ganteng = True
if saya_ganteng:
    print('Jika saya ganteng maka saya punya Banyak Cewe')
else:
    print('Jika saya tidak ganteng maka saya Jomblo')

print('#2.Percabangan 2 pilihan')
jenis_kelamin = 'laki-laki'
if jenis_kelamin == 'laki-laki':
    print('Jenis kelamin nya adalah laki-laki')
elif jenis_kelamin == 'perempuan':
    print('Jenis kelamin nya adalah perempuan')
else:
    print('jenis kelamin tidak diketahui')
print("---" * 10)
print("\n")
# 3.Perulangan
print("---" * 10)
print('#3.Perulangan')
print("---" * 10)
angka = 10
for a in range(1, angka + 1):
    # print('ini angka ',a)
    # bisa juga kaya gini
    print(f'ini angka {a}')
print("---" * 10)
