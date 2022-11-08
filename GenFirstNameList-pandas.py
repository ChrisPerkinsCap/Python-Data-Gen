import pandas

source_dir = "/Users/chris/Dev/Python-Data-Gen/CSV/"
source_file = "FirstNames-fr.csv"
target_file = "FirstNames-fr-Popularité.csv"
num_rows = 172

df = pandas.read_csv(source_dir + source_file,
            index_col="Popularité",
            header=0,
            names=['Prénom', 'Sexe', 'Popularité', 'Random Value']).drop('Random Value', axis=1)

df_sorted = df.sort_values(by=['Popularité'], ascending=False)

df_shortened = df_sorted.head(num_rows)

df_randomised = df_shortened.sample(num_rows)

print(df_randomised)

df_randomised.to_csv(source_dir + target_file)