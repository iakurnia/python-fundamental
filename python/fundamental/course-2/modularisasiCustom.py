"""
Program Modular dengan type directory berbeda (public in java)
"""
from segitiga.luas import luasSegitiga,info as info_segitiga
from persegipanjang.luas import luasPersegiPanjang,info as info_persegipanjang
print("---"*10)
print('#1.Modular Custom')
print("---"*10)

print(info_segitiga())
print(f'Luas Segitinya : {luasSegitiga(10,5)}')

print(info_persegipanjang())
print(f'Luas Segitinya : {luasPersegiPanjang(10,5)}')