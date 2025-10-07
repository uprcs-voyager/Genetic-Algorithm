import csv
import random
import pprint
import copy

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


peta_semester = {}

for data_mk in daftar_kelas :
    kode_string = data_mk['Kode_MK']
    mk_identifier = (data_mk['Kode_MK'], data_mk['Mata_Kuliah'], data_mk['Kelas'])

    if 'IF' in kode_string :
        semester  = kode_string[-3]
        peta_semester[mk_identifier] = semester
    else :
        grup_MKU = (data_mk['Mata_Kuliah'], data_mk['Kelas'])
        peta_semester[mk_identifier] = grup_MKU





def fitness_function(kromosom_individu, peta_semester) :
    jumlah_tabrakan = 0
    catatan_duplikat_dosen = set()
    catatan_duplikat_ruangan = set()
    catatan_duplikat_mahasiswa = set()

    for gen in kromosom_individu :
        pengenal_kelas = (gen['Kode_MK'], gen['Mata_Kuliah'], gen['Kelas'])
        semester = peta_semester[pengenal_kelas]
        
        
        tanda_dosen = (gen['Dosen'], gen['Hari'], gen['Sesi'])
        if tanda_dosen in catatan_duplikat_dosen :
            jumlah_tabrakan +=1
        else :
            catatan_duplikat_dosen.add(tanda_dosen)

        tanda_ruangan = (gen['Ruangan'], gen['Hari'], gen['Sesi'])
        if tanda_ruangan in catatan_duplikat_ruangan :
            jumlah_tabrakan +=1
        else :
            catatan_duplikat_ruangan.add(tanda_ruangan)

        pengenal_mahasiswa = (semester, gen['Hari'], gen['Sesi'])
        if pengenal_mahasiswa in catatan_duplikat_mahasiswa :
            jumlah_tabrakan +=1
        else :
            catatan_duplikat_mahasiswa.add(pengenal_mahasiswa)

    skor_bonus = 0
    hari_yang_ada_sesi = {gen['Hari'] for gen in kromosom_individu}
    jumlah_hari_kosong = 5 - len(hari_yang_ada_sesi)
    skor_bonus += jumlah_hari_kosong*100
    
    skor_awal = 1000
    penalti_tabrakan = 1000
    skor_final = skor_awal - (jumlah_tabrakan*penalti_tabrakan) + skor_bonus

    return skor_final


def seleksi_turnamen (populasi, fitness_score, UKURAN_TURNAMEN) :
    indeks_peserta = []

    for _ in range (UKURAN_TURNAMEN) :
        indeks_acak = random.randint(0, len(populasi) - 1)
        indeks_peserta.append(indeks_acak)

    indeks_terbaik = -1
    skor_terbaik = float('-inf')

    for indeks in indeks_peserta :
        skor = fitness_score[indeks]
        if skor > skor_terbaik :
            skor_terbaik = skor
            indeks_terbaik = indeks
        
    return populasi[indeks_terbaik]
    

def crossover(orang_tua1, orang_tua2) :
    titik_potong = random.randint(1, len(orang_tua1)- 1)

    anak1 = orang_tua1[:titik_potong] + orang_tua2[titik_potong:]
    anak2 = orang_tua2[:titik_potong] + orang_tua1[titik_potong:]
    return anak1, anak2



def mutation(kromosom, semua_dosen, semua_ruangan, semua_sesi, MUTATION_RATE) :
    for gen in range(len(kromosom)) :
        
        if random.random() < MUTATION_RATE :
            attribute_yang_diubah  = random.choice(['Dosen', 'Ruangan', 'Hari', 'Sesi'])

            if attribute_yang_diubah == 'Dosen' :
                kromosom[gen]['Dosen'] = random.choice(list(semua_dosen))
            elif attribute_yang_diubah == 'Ruangan' :
                kromosom[gen]['Ruangan'] = random.choice(list(semua_ruangan))
            elif attribute_yang_diubah == 'Sesi' :
                kromosom[gen]['Sesi'] = random.choice(list(semua_sesi))
            elif attribute_yang_diubah == 'Hari' :
                list_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat",]
                kromosom[gen]['Hari'] = random.choice(list(list_hari))
            
    return kromosom











# calling the chromosom function
# print("\n\n\n")


# print("\n -------- TEST DRIVE KROMOSOM -------\n")
# kromosom_pertama = membuat_kromosom_acak(semua_dosen, daftar_kelas, semua_ruangan, semua_sesi)

# populasi = buat_populasi_awal(ukuran_populasi)

# print("\n -------- FITNESS FUNCTION -------\n")
# fitness_score = []
# for kromosom in populasi :
#     skor_tabrakan = fitness_function(kromosom, peta_semester)
#     fitness_score.append(skor_tabrakan)
#     print(f"Jadwal/Kromosom ini memiliki jumlah tabrakan sebanyak: {skor_tabrakan}")
#     print(f"{fitness_score}")

# print("\n -------- PARENTS -------\n")

# orang_tua1 = seleksi_turnamen(populasi, fitness_score, UKURAN_TURNAMEN)
# orang_tua2 = seleksi_turnamen(populasi, fitness_score, UKURAN_TURNAMEN)
# print("\n--- Uji Coba Seleksi Turnamen ---")
# print("Berhasil memilih satu orang tua pemenang turnamen.")
# pprint.pprint(f"\nORANG TUA 1{orang_tua1}")
# pprint.pprint(f"\nORANG TUA 2{orang_tua2}")  

# print("\n -------- CROSSOVER-------\n")
# anak1, anak2 = crossover(orang_tua1, orang_tua2)
# print(f"\nAnak 1: {anak1}")
# print(f"\nAnak 2: {anak2}")


# print("\n -------- MUTATION-------\n")
# mutation = mutation(anak1, semua_dosen, semua_ruangan,  semua_sesi, MUTATION_RATE)
# print(f"\nTHE MUTATION: {mutation}")
# # pprint.pprint(kromosom_pertama)

# print(f"the first kromosom with {len(kromosom_pertama)} gen (jadwal kelas)")

# calling the chromosom function
# print("\n\n\n")


# print("\n -------- TEST DRIVE KROMOSOM -------\n")
# kromosom_pertama = membuat_kromosom_acak(semua_dosen, daftar_kelas, semua_ruangan, semua_sesi)

# populasi = buat_populasi_awal(ukuran_populasi)

# print("\n -------- FITNESS FUNCTION -------\n")
# fitness_score = []
# for kromosom in populasi :
#     skor_tabrakan = fitness_function(kromosom, peta_semester)
#     fitness_score.append(skor_tabrakan)
#     print(f"Jadwal/Kromosom ini memiliki jumlah tabrakan sebanyak: {skor_tabrakan}")
#     print(f"{fitness_score}")

# print("\n -------- PARENTS -------\n")

# orang_tua1 = seleksi_turnamen(populasi, fitness_score, UKURAN_TURNAMEN)
# orang_tua2 = seleksi_turnamen(populasi, fitness_score, UKURAN_TURNAMEN)
# print("\n--- Uji Coba Seleksi Turnamen ---")
# print("Berhasil memilih satu orang tua pemenang turnamen.")
# pprint.pprint(f"\nORANG TUA 1{orang_tua1}")
# pprint.pprint(f"\nORANG TUA 2{orang_tua2}")  

# print("\n -------- CROSSOVER-------\n")
# anak1, anak2 = crossover(orang_tua1, orang_tua2)
# print(f"\nAnak 1: {anak1}")
# print(f"\nAnak 2: {anak2}")


# print("\n -------- MUTATION-------\n")
# mutation = mutation(anak1, semua_dosen, semua_ruangan,  semua_sesi, MUTATION_RATE)
# print(f"\nTHE MUTATION: {mutation}")
# # pprint.pprint(kromosom_pertama)

# print(f"the first kromosom with {len(kromosom_pertama)} gen (jadwal kelas)")
    # if skor_terbaik_global == 0:
    #     print("\nSolusi optimal (0 tabrakan) ditemukan!")
    #     break


# skor_fitness_final = []
# for kromosom in population:
#     skor_fitness_final.append(fitness_function(kromosom, peta_semester))

# indeks_final_terbaik = skor_fitness_final.index(min(skor_fitness_final))
# kromosom_terbaik = population[indeks_final_terbaik]

GENERATION = 120;
ukuran_populasi = 500;
UKURAN_TURNAMEN = 50;
MUTATION_RATE = 0.08;

# variable pelacak player global
kromosom_terbaik_global = None
skor_terbaik_global = float('-inf')

population = buat_populasi_awal(ukuran_populasi)

for i in range(GENERATION) :
    fitness_score = [fitness_function(kromosom, peta_semester) for kromosom in population]
    skor_terbaik_generasi_ini = max(fitness_score) 
    if skor_terbaik_generasi_ini > skor_terbaik_global :
        skor_terbaik_global = skor_terbaik_generasi_ini
        indeks_terbaik = fitness_score.index(skor_terbaik_global)
        kromosom_terbaik_global = population[indeks_terbaik]
    
    populasi_baru = []
    # ELITISME
    if kromosom_terbaik_global :
        populasi_baru.append(kromosom_terbaik_global)

    while len(populasi_baru) < ukuran_populasi :
        orang_tua1 = seleksi_turnamen(population, fitness_score, UKURAN_TURNAMEN)
        orang_tua2 = seleksi_turnamen(population, fitness_score, UKURAN_TURNAMEN)

        anak1, anak2 = crossover(orang_tua1, orang_tua2)

        anak1_copy = copy.deepcopy(anak1)
        mutasi_anak1 = mutation(anak1_copy, semua_dosen, semua_ruangan, semua_sesi, MUTATION_RATE)
        populasi_baru.append(mutasi_anak1)

        if len(populasi_baru) < ukuran_populasi :
            anak2_copy = copy.deepcopy(anak2)
            mutasi_anak2 = mutation(anak2_copy, semua_dosen, semua_ruangan, semua_sesi, MUTATION_RATE)
            populasi_baru.append(mutasi_anak2)
    population = populasi_baru


    skor_terbaik_generasi_ini = max(fitness_score)
    print(f"Generasi {i+1} | Skor fitness Terbaik Sejauh Ini: {skor_terbaik_global}")

    # if skor_terbaik_global == 0:
    #     print("\nSolusi optimal (0 tabrakan) ditemukan!")
    #     break


# skor_fitness_final = []
# for kromosom in population:
#     skor_fitness_final.append(fitness_function(kromosom, peta_semester))

# indeks_final_terbaik = skor_fitness_final.index(min(skor_fitness_final))
# kromosom_terbaik = population[indeks_final_terbaik]

print("\n--- HASIL AKHIR SETELAH EVOLUSI ---")
print(f"Jadwal terbaik memiliki {skor_terbaik_global} skor fitness.")
pprint.pprint(kromosom_terbaik_global)

print("\n\n\n")
