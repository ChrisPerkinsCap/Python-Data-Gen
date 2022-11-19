from RandomNamesGenerator import RandomNamesGenerator as RNG
import copy
from datetime import datetime
from faker import Faker

num_rows = 172
dt = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
source_dir = "./CSV/"
target_file = f"Depatures-{dt}.csv"
fnames_source_file = "FirstNames-Popularity-fr.csv"
fnames_target_file = f"FirstNames-Popularity-fr-{dt}.csv"
fnames_drop_columns = ["Popularity"]

fnames_rename_columns = {'FirstName': 'Prénom', 'Gender': 'Sexe'}

fnames_sort_columns = ["Popularity"]
fnames_final_order = ["Prénom", "Sexe", "Popularity"]
fnames_columns_order = ["Popularity", "Sexe", "Prénom"]

lnames_source_file = "LastNames-Popularity-fr.csv"
lnames_target_file = f"LaststNames-Popularity-fr-{dt}.csv"
lnames_drop_columns = ["Popularity"]

lnames_rename_columns = {'patronyme': 'Patronym', 'LastNameCount': 'Popularity'}

lnames_sort_columns = ["Popularity"]
lnames_final_order = ["Patronym", "Popularity"]
lnames_columns_order = ["Popularity", "Patronym"]

# sort_columns = ["NameCount"]
# final_sort = ["name", "sex", "NameCount"]
# columns_order = ["NameCount", "sex", "name"]


FNG = RNG(fnames_rename_columns, num_rows, source_dir, fnames_source_file)

# FNG.print_data_frame()


fn = FNG.get_data()
# print(fn)
# tn = GenerateRandomFirstNamesCSV.return_percentage(fn, fnames_sort_columns, 20, False)
# print(tn)
fn = RNG.prepare_data_frame(FNG, fnames_columns_order, None, fnames_final_order, fnames_sort_columns, 10, False)

print(fn)

print("#### LAST NAMES ####")

LNG = RNG(lnames_rename_columns, num_rows, source_dir, lnames_source_file)

# LNG.print_data_frame()


ln = LNG.get_data()

ln = RNG.prepare_data_frame(LNG, lnames_columns_order, None, lnames_final_order, lnames_sort_columns, 30, False)

# print(ln)

LastNames = ln.Patronym.values.tolist()
patronymes = list()

for i in LastNames:
    patronymes.append(str(i).capitalize())

fn.insert(0, "Nom", patronymes)
print(fn)

# GenerateRandomFirstNamesCSV.write_to_csv(df, source_dir, target_file)

GGID = list()

f = Faker()

for _ in range(num_rows):
    GGID.append(f.unique.numerify(text='%#######'))


fn.insert(0, 'GGID', GGID)

# print(fn)


# for i in range(len(GGUID)):
#     print(GGUID[i])


# GGUID = list()

# for _ in range(10):
#     GGUID.append(fake.numerify)




# uuid = UUID(bytes=32)

# print(uuid)
