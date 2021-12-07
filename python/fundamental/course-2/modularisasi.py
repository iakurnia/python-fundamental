"""
Program menghitung Segitiga
Luas Segitiga = alas x tinggi /2
"""
print("---" * 10)
print('#1.Modular')
print("---" * 10)
print('Menghitung Luas Segitiga tanpa Modular')
alas = 5
tinggi = 10
luas = alas * tinggi / 2
print(f'Alas : {alas} x Tinggi : {tinggi} Luasnya = {luas}')

print('\nMenghitung Luas Segitiga dengan Modular')


def luasSegitiga(param1, param2):
    print(f'Alas : {param1} \nTinggi : {param2}')
    luassegitiga = param1 * param2 / 2
    return luassegitiga


print(f'Luasnya = {luasSegitiga(10, 20)}')
