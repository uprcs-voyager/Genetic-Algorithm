import csv
import random
import pprint

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
                      
                        # print(f"Dosen: {dosen_cleaned}")
                        # print(f"Hari: {day} || index {day_index} ||")
                        # print(f"Sesi: {sesi_cleaned}")
                        # print(f"Ruangan: {replace_room_cleaned}\n")

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
                        # print(f"This is the dictionary: {dictionary}")
                        
                        data_jadwal_clean.append(dictionary)

                        break;
    #     print(parts) 
    

    #     print(lines)
    #     print('\n')
    # print(data_jadwal_clean)
    # print('\n')

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
# print(f"Jumlah jadwal yang berhasil di-parse: {len(data_jadwal_clean)}")
# print(f"Jumlah kelas unik yang harus dijadwalkan: {len(daftar_kelas)}")
# print(f"Jumlah dosen unik: {len(semua_dosen)}")
# print(f"Jumlah ruangan unik: {len(semua_ruangan)}")
# print(f"Jumlah sesi unik: {len(semua_sesi)}")


def membuat_kromosom_acak(semua_dosen, daftar_kelas, semua_ruangan, semua_sesi):
    kelas = daftar_kelas
    semua_dosen = semua_dosen
    semua_ruangan = semua_ruangan
    semua_sesi = semua_sesi
    semua_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat"]
    kromosom = []
    
    for kelas in daftar_kelas :
        gen_dictionary = {
            'Kode_MK': '',
            'Mata_Kuliah': '',
            'Kelas': '',
            'Dosen': '',
            'Hari': '',
            'Sesi': '',
            'Ruangan': ''
        }
        gen_dictionary['Kode_MK'] = kelas['Kode_MK']
        gen_dictionary['Mata_Kuliah'] = kelas['Mata_Kuliah']
        gen_dictionary['Kelas'] = kelas['Kelas']
        gen_dictionary['Dosen'] = random.choice(list(semua_dosen))
        gen_dictionary['Hari'] = random.choice(semua_hari)
        gen_dictionary['Sesi'] = random.choice(list(semua_sesi))
        gen_dictionary['Ruangan'] = random.choice(list(semua_ruangan))

        
        kromosom.append(gen_dictionary)
    return kromosom



def buat_populasi_awal (ukuran_populasi) :
    population = []

    for _ in range (ukuran_populasi) :
        kromosom_baru = membuat_kromosom_acak(semua_dosen, daftar_kelas, semua_ruangan, semua_sesi)
        population.append(kromosom_baru)
    
    return population;


def fitness_function(kromosom_individu) :
    jumlah_tabrakan = 0
    catatan_duplikat_dosen = set()
    catatan_duplikat_ruangan = set()

    for gen in kromosom_individu :
        gen_identifier1 = (gen['Dosen'], gen['Hari'], gen['Sesi'])
        gen_identifier2 = (gen['Ruangan'], gen['Hari'], gen['Sesi'])
    
        if gen_identifier1 not in catatan_duplikat_dosen :
            catatan_duplikat_dosen.add(gen_identifier1)
        else :
            jumlah_tabrakan +=1

        if gen_identifier2 not in catatan_duplikat_ruangan :
            catatan_duplikat_ruangan.add(gen_identifier2)
        else :
            jumlah_tabrakan +=1
    return jumlah_tabrakan
    



# calling the chromosom function
print("\n -------- TEST DRIVE KROMOSOM -------\n")
kromosom_pertama = membuat_kromosom_acak(semua_dosen, daftar_kelas, semua_ruangan, semua_sesi)
ukuran_populasi = 100;
populasi = buat_populasi_awal(ukuran_populasi)

for kromosom in populasi :
    skor_tabrakan = fitness_function(kromosom)
    print(f"Jadwal/Kromosom ini memiliki jumlah tabrakan sebanyak: {skor_tabrakan}")


pprint.pprint(kromosom_pertama)

print(f"the first kromosom with {len(kromosom_pertama)} gen (jadwal kelas)")

print("\n\n\n")
print(f"\n--- Membuat Populasi Awal ---")
print(f"Berhasil membuat populasi dengan {len(populasi)} individu (kromosom).")
print(f"Setiap individu memiliki {len(populasi[0])} gen (jadwal kelas).")

print("\n\n\n")
