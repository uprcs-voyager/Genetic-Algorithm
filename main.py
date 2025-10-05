import csv
import pandas


# IMPORTING DATA USING CSV
print("Data read using csv DictReader")
print("\n")
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



                        break;
        print(parts) 
     
        print(lines)
        print('\n')

print("\n\n\n")
# # IMPORTING DATA USING PANDAS
# print("Data read using pandas")
# print("\n")
# excelPanda = pandas.read_excel('dataset/Jadwal Kuliah IF ITK.xlsx')
# print(excelPanda)
