import random 


BARANG = {
    "A" : {"berat": 2, "nilai": 3},
    "B" : {"berat": 3, "nilai": 4}, 
    "C" : {"berat": 4, "nilai": 5},
    "D" : {"berat": 5, "nilai": 6},
    "E" : {"berat": 9, "nilai": 7},
    "F" : {"berat": 7, "nilai": 8},
    "G" : {"berat": 8, "nilai": 9},
}

NAMA_BARANG = list(BARANG.keys())
JUMLAH_BARANG = len(BARANG)
KAPASITAS_MAXIMUM  = 20


# Parameter genetic algorithm 
UKURAN_POPULASI  = 200
JUMLAH_GENERASI = 200
LAJU_MUTASI = 0.02
JUMLAH_TURNAMEN = 8


# main function 

def buat_individu() :
    "Creating random chromosom biner"
    return[random.randint(0,1) for _ in range(JUMLAH_BARANG)]

def calculate_fitness(individu) :
    "menghitung nilai total dari benda yang dibawa dengan pinalti jika kelebihan berat"
    total_berat = 0
    total_nilai = 0
    for i, gen in enumerate(individu):
        if gen == 1 :
            nama = NAMA_BARANG[i]
            total_berat += BARANG[nama]["berat"]
            total_nilai += BARANG[nama]["nilai"]
    
    if total_berat > KAPASITAS_MAXIMUM :
        return 0;
    else :
        return total_nilai
    

def selection(populasi) :
    "Memilih individu terbaik berdasarkan hasil dari turnamen"
    tournament_participant = random.sample(populasi, JUMLAH_TURNAMEN)
    
    # mengurutkan peserta turnamen berdasarkan nilai fitness yang tertinggi 
    tournament_participant.sort(key=lambda individu: calculate_fitness(individu), reverse=True)

    return tournament_participant[0]

def crossover(parent1, parent2) :
    "menggabungkan 2 orang tua untuk menhasilkan offspring baru"
    titik_potong = random.randint(1, JUMLAH_BARANG-1)

    offspring1 = parent1[:titik_potong] + parent2[titik_potong:]
    offspring2 = parent2[:titik_potong] + parent1[titik_potong:]

    return offspring1, offspring2

def mutasi(individu) :
    # perlu di ingat perubahan secara bit efektif digunakan jika representasi kromosom adalah biner
    "mengubah gen (bit) secara acak based on mutation speed" 
    for i in range (JUMLAH_BARANG) :
        if random.random() < LAJU_MUTASI :
            individu[i] = 1-individu[i]
    return individu


def run_genetic() :
    # membuat populasi
    populasi = [buat_individu() for _ in range(UKURAN_POPULASI)]

    # menetapkan variable placeholder
    global_best_individual = None
    global_best_fitness = -1

 

    # siklus evolusi
    for gen in range (JUMLAH_GENERASI) :

        # menghitung fitness populasi saat ini
        populasi.sort(key = lambda temp: calculate_fitness(temp), reverse=True)

        # mengambil individual terbaik dari generasi ini
        current_best_individual = populasi[0]
        # menghitung fitness dari individu terbaik 
        current_best_fitness = calculate_fitness(current_best_individual)

        #  meng-update nilai variable placeholder dengan nilai yang sudah di-update
        if current_best_fitness > global_best_fitness :
            global_best_fitness = current_best_fitness
            global_best_individual = current_best_individual
        
        print(f"Generasi ke {gen+1}: Fitness Terbaiknya adalah: {global_best_fitness}")

        # Membuat generasi baru 
        populasi_baru = []
        populasi_baru.append(global_best_individual)

        while len(populasi_baru) < UKURAN_POPULASI :
            # melakukan seleksi dua parent 
            parent1 = selection(populasi)
            parent2 = selection(populasi)

            # crossover melakukan pertukaran
            offspring1, offspring2 = crossover(parent1, parent2)

            # melakukan mutasi
            populasi_baru.append(mutasi(offspring1))
            if len (populasi_baru) < UKURAN_POPULASI :
                populasi_baru.append(mutasi(offspring2))
            
        populasi = populasi_baru    
    
    return global_best_individual

# MENG EKSEKUSI PROGRAM 

if __name__ == "__main__" :
    best_solution = run_genetic()

    print("EVOLUTION COMPLETED")
    print("\n\n")
    print(f"Best chromosome: {best_solution}")

    total_berat_akhir = 0
    total_nilai_akhir = 0
    barang_terpilih = []

    for i, gen in enumerate (best_solution) :
        if gen == 1 :
            nama                =  NAMA_BARANG[i]
            barang_terpilih.append(nama)
            total_berat_akhir   += BARANG[nama]["berat"]
            total_nilai_akhir   += BARANG[nama]["nilai"]
    
    print(f"barang yang dibawa adalah: {','.join(barang_terpilih)} ")
    print(f"Total berat yang dibawa adalah: {total_berat_akhir} dan berat maksimal adalah {KAPASITAS_MAXIMUM}")
    print(f"Total nilai akhir adalah: {total_nilai_akhir}")


