import csv


# IMPORTING DATA USING CSV
print("Data read using csv DictReader")
print("\n")

data_jadwal_clean = []




with open('dataset/Jadwal Kuliah IF ITK - Detail.csv', mode= 'r') as file :
    
    csvFile = csv.DictReader(file)
    for lines in csvFile:
        specific_string = lines['Dosen, Hari, Sesi']
        if specific_string :
            parts = specific_string   
            days = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
            for day in days :
                day_index = specific_string.find(day)
                if day_index != -1 :
                        get_lines = parts
                        get_lines = get_lines[:day_index]
                        dosen_unclean = get_lines
                        dosen_cleaned = dosen_unclean.strip()
                        
                        ruangan_index = specific_string.find("Ruang:")
                        start_index = ruangan_index
                        kapasitas_index = specific_string.find(", Kapasitas")
                        ruangan = specific_string[start_index:kapasitas_index]
                        replace_room_uncleaned = ruangan.replace("Ruang: ", "")
                        replace_room_cleaned = replace_room_uncleaned.strip()

                        ruangan_index = specific_string.find("Ruang:")
                        start_index = day_index + len(day)
                        end_index = ruangan_index
                        sesi = specific_string[start_index:end_index]
                        sesi_uncleaned = sesi.replace(",","")
                        sesi_cleaned = sesi_uncleaned.strip()
                      
                        print(f"Dosen: {dosen_cleaned}")
                        print(f"Hari: {day} || index {day_index} ||")
                        print(f"Sesi: {sesi_cleaned}")
                        print(f"Ruangan: {replace_room_cleaned}\n")

                        # Dictionary
                        dictionary = {
                             'Kode_MK': '',
                             'Mata_Kuliah': '',
                             'Kelas': '',
                             'Dosen': '',
                             'Hari': '',
                             'Sesi': '',
                             'Ruangan': '',
                        }
                        dictionary['Kode_MK'] = lines['Kode MK']
                        dictionary['Mata_Kuliah'] = lines['Mata Kuliah']
                        dictionary['Kelas'] = lines['Kelas']
                        dictionary['Dosen'] = dosen_cleaned
                        dictionary['Hari'] = day
                        dictionary['Sesi'] = sesi_cleaned
                        dictionary['Ruangan'] = replace_room_cleaned
                        print(f"This is the dictionary: {dictionary}")
                        
                        data_jadwal_clean.append(dictionary)

                        break;
        print(parts) 
    

        print(lines)
        print('\n')
    print(data_jadwal_clean)
    print('\n')

daftar_kelas = []
kelas_yang_sudah_dicatat = set()

semua_dosen = set()
semua_ruangan = set()
semua_sesi = set()

for data in data_jadwal_clean :
        
    identifier = (data['Kode_MK'], data['Mata_Kuliah'], data['Kelas'])
    
    if identifier not in kelas_yang_sudah_dicatat :
            kelas_yang_sudah_dicatat.add(identifier)

            dictionary_new = {
                'Kode_MK': data['Kode_MK'],
                'Mata_Kuliah': data['Mata_Kuliah'], 
                'Kelas': data['Kelas']
                }    
            daftar_kelas.append(dictionary_new)
    semua_dosen.add(data['Dosen'])
    semua_ruangan.add(data['Ruangan'])
    semua_sesi.add(data['Sesi'])

            
print(f"Ini dictionary yepyep: {daftar_kelas}")
        

# debugging
print(f"Jumlah jadwal yang berhasil di-parse: {len(data_jadwal_clean)}")
print(f"Jumlah kelas unik yang harus dijadwalkan: {len(daftar_kelas)}")
print(f"Jumlah dosen unik: {len(semua_dosen)}")
print(f"Jumlah ruangan unik: {len(semua_ruangan)}")
print(f"Jumlah sesi unik: {len(semua_sesi)}")



print("\n\n\n")
