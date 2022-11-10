from GenerateRandomFirstNamesCSV import GenerateRandomFirstNamesCSV

source_dir = "./CSV/"
source_file = "FirstNames-fr.csv"
target_file = "FirstNames-fr-Popularité.csv"
drop_column = "Random Value"
sort_column = "Popularité"
num_rows = 172

RG = GenerateRandomFirstNamesCSV(num_rows, source_dir, source_file, target_file)

df = RG.process_csv_file(source_dir, source_file, num_rows, drop_column, sort_column)

RG.print_data_frame()

