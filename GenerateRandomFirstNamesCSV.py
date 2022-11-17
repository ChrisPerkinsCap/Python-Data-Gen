from os.path import exists
import pandas
from pandas import DataFrame
import copy
from datetime import datetime

class GenerateRandomFirstNamesCSV:
    
    ######## Constructor ########

    def __init__(self, columns_order=list(), drop_columns=list(), final_sort=list(), num_rows=int,
                    sort_columns=list(), source_dir=str, source_file=str, target_file=str):

        if columns_order is None:
            columns_order = ["Popularity", "Gender", "FirstName"]
        
        self.set_columns_order(columns_order)

        if drop_columns is None:
            drop_columns = ["NameCount"]
        
        self.set_drop_columns(drop_columns)

        if final_sort is None:
            final_sort = ["FirstName", "Gender", "Popularity"]
        
        self.set_final_sort(final_sort)

        if num_rows is None:
            num_rows = 0
        
        self.set_num_rows(num_rows)

        if sort_columns is None:
            sort_columns = ["Popularity"]
        
        self.set_sort_columns(sort_columns)

        if source_dir is None:
            source_dir = "./CSV/"
        
        self.set_source_dir(source_dir)

        if source_file is None:
            source_file = "FirstNames-Popularity-fr.csv"
        
        self.set_source_file(source_file)

        if target_file is None:
            dt = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
            target_file = f"FirstNames-Popularity-fr{dt}.csv"
        
        self.set_target_file(target_file)

        data = GenerateRandomFirstNamesCSV.read_file(source_dir, source_file)
        # print(data)
        self.set_data(data)

    
    ### GETTERS and SETTERS ###
    
    def get_columns_order(self) -> list():
        return copy.deepcopy(self._columns_order)
    
    def set_columns_order(self, columns_order=list()) -> None:
        self._columns_order = columns_order
    
    def get_drop_columns(self) -> list():
        return copy.deepcopy(self._drop_columns)
    
    def set_drop_columns(self, drop_columns=list()) -> None:
        self._drop_columns = drop_columns
    
    def get_final_sort(self) -> list():
        return copy.deepcopy(self._final_sort)
    
    def set_final_sort(self, final_sort=list()) -> None:
        self._final_sort = final_sort
    
    def get_num_rows(self) -> int:
        return copy.copy(self._num_rows)
    
    def set_num_rows(self, num_rows=int) -> None:
        self._num_rows = num_rows
    
    def get_sort_columns(self) -> list():
        return copy.deepcopy(self._sort_columns)
    
    def set_sort_columns(self, sort_columns=list()) -> None:
        self._sort_columns = sort_columns
    
    def get_source_dir(self) -> str:
        return copy.copy(self._source_dir)
    
    def set_source_dir(self, source_dir=str) -> None:
        self._source_dir = source_dir
    
    def get_source_file(self) -> str:
        return copy.copy(self._source_file)
    
    def set_source_file(self, source_file=str) -> None:
        self._source_file = source_file
    
    def get_target_file(self) -> str:
        return copy.copy(self._target_file)
    
    def set_target_file(self, target_file=str) -> None:
        self._target_file =target_file
    
    def get_data(self) -> DataFrame:
        return copy.deepcopy(self._data)
    
    def set_data(self, data=DataFrame) -> None:
        self._data = data
    
    ### INSTANCE METHODES ###

    def order_by_popularity(self, ascend=bool) -> DataFrame:
        data_frame = self.get_data()
        return data_frame.sort_values(by="Popularity", ascending=ascend, kind="mergesort")
    
    def remove_column(self, column_name=str) -> DataFrame:
        data_frame = self.get_data()
        column = [column_name]
        new_frame = GenerateRandomFirstNamesCSV.drop_data_column(data_frame, column)
        self.set_data(new_frame)
        return new_frame

    def print_data_frame(self) -> None:
        print(self.get_data())

    ### CLASS METHODES ###

    @classmethod
    def read_file(cls, source_dir=str, source_file=str) -> DataFrame:
        return pandas.read_csv(source_dir + source_file)

    @classmethod
    def read_file_rename_columns(cls, source_dir=str, source_file=str, column_names=list()) -> DataFrame:
        return pandas.read_csv(source_dir + source_file, header=0, names=column_names)
    
    @classmethod
    def drop_data_column(cls, data_table=DataFrame, drop_column=list()) -> DataFrame:
        return data_table.drop(drop_column, axis=1)

    @classmethod
    def sort_data_table(cls, data_table=DataFrame, sort_columns=list(), columns_order=list()) -> DataFrame:
        return data_table.sort_values(by=sort_columns, ascending=False, kind="mergesort")[columns_order]
    
    @classmethod
    def truncate_data_table(cls, data_table=DataFrame, num_rows=int) -> DataFrame:
        return data_table.head(num_rows)

    @classmethod
    def randomize_rows(cls, data_table=DataFrame, num_rows=int) -> DataFrame:
        return data_table.sample(num_rows)

    @classmethod
    def process_csv_file(cls, columns_order=list(), drop_columns=list(), final_sort=list(), num_rows=int,
                            sort_columns=list(), source_dir=str, source_file=str) -> DataFrame:
        data = cls.read_file(source_dir, source_file)
        data = cls.sort_data_table(data, sort_columns, columns_order)
        data = cls.truncate_data_table(data, num_rows)
        data = cls.sort_data_table(data, sort_columns, final_sort)
        data = cls.drop_data_column(data, drop_columns)
        data = cls.randomize_rows(data, num_rows)
        return data
    
    @classmethod
    def write_to_csv(cls, data=DataFrame, target_directory=str, target_file=str) -> bool:
        if target_file is None:
            dt = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
            target_file = f"FirstNames-Popularity-fr{dt}.csv"
        
        if target_directory is None:
            target_directory = "./CSV/"

        file_path = target_directory + target_file
        data.to_csv(file_path, index=False)
        return exists(file_path)