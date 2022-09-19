import json

with open('mahasiswa.json','r') as file:
    data =  json.load(file)

total = int(input('Masukkan jumlah mahasiswa baru : '))

for i in range(total):
    nama = input('Masukkan nama Anda : ')
    hobi = int(input('Masukkan Jumlah hobi : '))
    for x in range (1,hobi+1):
        tampungan = []
        hobi = (input('Masukkan Hobi ke-'+ str(x) + ' : '))
        tampungan.append(hobi)
    prestasi = input('Masukkan Prestasi Anda : ')
    print('=== Data berhasil ditambahkan === \n')

a = {"nama": nama, 'biodata' : {"hobi": hobi, "prestasi": prestasi}}
