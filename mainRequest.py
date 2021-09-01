import requests

try:
    url = 'https://detik.com'
    r = requests.get('%s' % url)
    if r.status_code == 200:
        print(f'Response code {r.status_code}')
        print(f'Content : {r.text}')
    else:
        print(f'Gagal Response code : {r.status_code}')
except Exception as e:
    print(f'gagal load request : {e}')

print('Proses Selesai')
