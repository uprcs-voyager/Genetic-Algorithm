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
                string_index = specific_string.find(day)
                if string_index != -1 :
                        print(f"Hari: {day} Berada pada index: {string_index}")
                        get_lines = parts
                        get_lines = get_lines[:string_index]
                        dosen_kotor = get_lines
                        print(f"Dosen: {get_lines}\n")
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
