"""
Program menghitung Segitiga
Luas Segitiga = alas x tinggi /2
"""
print("---"*10)
print('#1.Modular')
print("---"*10)
print('Menghitung Luas Segitiga tanpa Modular')
alas = 5
tinggi = 10
luas = alas * tinggi / 2
print(f'Alas : {alas} x Tinggi : {tinggi} Luasnya = {luas}')

print('\nMenghitung Luas Segitiga dengan Modular')
def luasSegitiga(alas,tinggi):
    luas = alas * tinggi / 2
    print(f'Alas : {alas} \nTinggi : {tinggi}')
    return luas;

print(f'Luasnya = {luasSegitiga(10,20)}')