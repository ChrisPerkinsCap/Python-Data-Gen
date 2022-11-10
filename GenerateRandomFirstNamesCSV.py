from os.path import exists
import pandas
from pandas import DataFrame

class GenerateRandomFirstNamesCSV:
    
    # source_dir = "/Users/chris/Dev/Python-Data-Gen/CSV/"
    # source_file = "FirstNames-fr.csv"
    # target_file = "FirstNames-fr-Popularité.csv"
    # num_rows = 172

    def __init__(self, num_rows, source_dir, source_file, target_file):

        self._num_rows = num_rows
        self._source_dir = source_dir
        self._source_file = source_file
        self._target_file = target_file
        self._data = self.read_file(self, source_dir, source_file)
    
    def get_num_rows(self):
        return self._num_rows
    
    def set_num_rows(self, num_rows=int):
        self._num_rows = num_rows
    
    def get_source_dir(self):
        return self._source_dir
    
    def set_source_dir(self, source_dir=str):
        self._source_dir = source_dir
    
    def get_source_file(self):
        return self._source_file
    
    def set_source_file(self, source_file=str):
        self.get_source_file = source_file
    
    def get_target_file(self):
        return self._target_file
    
    def set_target_file(self, target_file=str):
        self._target_file =target_file
    
    def get_data(self):
        return self._data
    
    def set_data(self, data=DataFrame):
        self._data = data
    
    def read_file(self, source_dir=str, source_file=str):
        data = pandas.read_csv(source_dir + source_file,
            index_col="Popularité",
            header=0,
            names=['Prénom', 'Sexe', 'Popularité', 'Random Value'])
        return data
    
    def drop_data_column(self, data_table=DataFrame, drop_column=str):
        data = data_table.drop(drop_column, axis=1)
        return data

    def sort_data_table(self, data_table=DataFrame, sort_column=str):
        data = data_table.sort_values(by=[sort_column], ascending=False)
        return data
    
    def truncate_data_table(self, data_table=DataFrame, num_rows=int):
        data = data_table.head(num_rows)
        return data

    def randomize_rows(self, data_table=DataFrame, num_rows=int):
        data = data_table.sample(num_rows)
        return data

    def process_csv_file(self, source_dir=str, source_file=str, num_rows=int, drop_column=str, sort_column=str):
        data = self.read_file(source_dir, source_file)
        data = self.drop_data_column(data, drop_column)
        data = self.sort_data_table(data, sort_column)
        data = self.truncate_data_table(data, num_rows)
        data = self.randomize_rows(data, num_rows)
        return data
    
    def print_data_frame(self, data=DataFrame):
        if data is None:
            print(self.get_data())
        else:
            print(data)
    
    def write_data_frame(self, data=DataFrame, target_file=str):
        path = self.get_source_dir() + target_file
        data.to_csv(path)
        file_exists = exists(path)
        return file_exists