"""
Type data dictionary sekedar menghubungkan KEY dan VALUE
KVP         = Key Value Pair
Dictionary  = Kamus
"""
print('---' * 10)
print('Type Data Dictionary')
print('---' * 10)
print('\n1.Type Data Dictionary Basic')
kamus_ind_eng = {'Ayah': 'Father', 'Ibu': 'Mother', 'Anak': 'Son'}
print(kamus_ind_eng)
print(kamus_ind_eng['Anak'])

print('\n2.Type Data Dictionary Custom')
dataKeluarga = {
    'Ayah': 'Ia Kurnia',
    'Ibu': 'Yuni Safitri',
    'Anak': [
        {'nama': 'Kheyra', 'umur': 10}, {'nama': 'Aqila', 'umur': 7}, {'nama': 'Karima', 'umur': 4}
    ],
    'Cucu': ['Caca', 'Cici', 'Cucu']
}
print(dataKeluarga)
print(f"Nama saya {dataKeluarga['Ayah']}")
print(f"Anak Anak saya {dataKeluarga['Anak']}")
print(f"Anak ke 2 saya {dataKeluarga['Anak'][1]}")
print(f"Cucu Cucu saya {dataKeluarga['Cucu']}")
print(f"Cucu ke 2 saya {dataKeluarga['Cucu'][1]}")
print(f"Anak Pertama saya adalah {dataKeluarga['Anak'][0]['nama']} dan umurnya adalah {dataKeluarga['Anak'][0]['umur']}")