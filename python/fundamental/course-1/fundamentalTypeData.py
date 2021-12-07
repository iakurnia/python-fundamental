# Type data skalar / type data sederhana
print("---" * 10)
print('#1.Type Data Sederhana')
print("---" * 10)
nama1 = 'Ia'
nama2 = 'Kurnia'
print(nama1)
print(nama2)
print("---" * 10)
print("\n")

print("---" * 10)
print('#2.Type Data List')
print("---" * 10)
listNama = ['Ia', 'Kurnia']
print(listNama)
listNama.append('Karima')
print(listNama)

print('\nSapa Anak kedua')
print(f'Hallo : {listNama[1]}')

print('\nSapa Semua Anak pakai for biasa')
for a in listNama:
    print(f'Halo : {a}')

print('\nSapa Semua Anak dengan for Custom')
for a in range(0, len(listNama)):
    print(f'{a + 1}.Hallo : {listNama[a]}')
