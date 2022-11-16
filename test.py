from GenerateRandomFirstNamesCSV import GenerateRandomFirstNamesCSV
import copy
from datetime import datetime

source_dir = "./CSV/"
source_file = "FirstNames-Popularity-fr.csv"
target_file = "FirstNames-Popularity-fr.csv"
drop_columns = ["NameCount", "Rand"]
# sort_columns = ["name","sex","NameCount", "Rand"]
sort_columns = ["Popularity"]
final_sort = ["FirstName", "Gender", "Popularity"]
columns_order = ["Popularity", "Gender", "FirstName"]
# drop_columns = ["Random Value"]
# sort_columns = ["Prénom", "sexe", "Popularité", "Random Value"]
# columns_order = ["Popularité", "sexe", "Prénom", "Random Value"]
num_rows = 172

RG = GenerateRandomFirstNamesCSV(columns_order, drop_columns, final_sort, num_rows,
                                 sort_columns, source_dir, source_file)
# print(len(drop_columns))
# df = RG.process_csv_file(columns_order, drop_columns, final_sort, num_rows,
#                          sort_columns, source_dir, source_file)

RG.print_data_frame()

# data = GenerateRandomFirstNamesCSV.process_csv_file(columns_order, drop_columns,
#                                     final_sort, num_rows, sort_columns, source_dir, source_file)

# print(data.describe())
# print(data)

# fresh_data = copy.copy(data.reindex())

# print(fresh_data)

fresh_data = RG.remove_column("Rand")

fresh_data.rename(columns={'name':'FirstName', 'sex':'Gender', 'NameCount':'Popularity'}, inplace=True)

RG.print_data_frame()

print(RG.get_data())

now_time = datetime.now()
now_time_ft = now_time.strftime("%d-%m-%Y_%H:%M:%S")

print(now_time_ft)

# GenerateRandomFirstNamesCSV.write_to_csv(
#     fresh_data, source_dir, "FirstNames-Popularity-fr.csv")
