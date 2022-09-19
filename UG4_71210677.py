import json

with open('mahasiswa.json','r') as datafile:
    data =  json.load(datafile)
    inputan = int(input('Masukkan jumlah mahasiswa baru : '))

    for i in range(0, inputan):
        inputan_nama = input('Masukkan nama Anda : ')
        list_satu = []
        dct_kosong = {}
        jumlah = int(input('Masukan Jumlah hobi: '))
        list_dua = []

        for a in range(1,jumlah+1):
            inputan_dua = input("Masukan Hobi ke-{index} : ".format(index=a))
            list_satu.append(inputan_dua)
        juara = input("Masukkan Prestasi Anda : ")
        list_satu.append({"BioData":{"Hobi":list_satu,"Prestasi":juara}})
        data[inputan_nama] = list_satu

        print("=== Data berhasil ditambahkan ===")
        print()

with open('mahasiswa.json', 'w') as datafile:
    json.dump(data, datafile)
