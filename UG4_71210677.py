import json

with open('mahasiswa.json','r') as file:
    data =  json.load(file)

total = int(input('Masukan jumlah mahasiswa baru : '))

for i in range(total):
    nama = input('Masukan nama Anda : ')
    hobi = int(input('Masukan Jumlah hobi : '))
    for x in range (1,hobi+1):
        tampungan = []
        hobi = (input('Masukan Hobi ke-'+ str(x) + ' : '))
        tampungan.append(hobi)
    prestasi = input('Masukan Prestasi Anda : ')
    print('=== Data berhasil ditambahkan === \n')

a = {"nama": nama, 'biodata' : {"hobi": hobi, "prestasi": prestasi}}