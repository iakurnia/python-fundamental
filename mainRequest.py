import requests

try:
    r = requests.get('https://goog le.com')
    print(r.status_code)
    if r.status_code == 200:
        print("berhasil masuk")
        print(r.text)
    else:
        print("gagal request")
except :
    print("gagal load request")

