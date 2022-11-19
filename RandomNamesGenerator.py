from __future__ import annotations
import copy
from datetime import datetime
from decimal import Decimal
from os.path import exists

import pandas
from pandas import DataFrame


class RandomNamesGenerator:

    ######## Constructor ########

    def __init__(self, column_names=list(), num_rows=int, source_dir=str, source_file=str):

        if len(column_names) > 0:
            self.set_column_names(column_names)

        if num_rows is None:
            num_rows = 0

        self.set_num_rows(num_rows)

        if source_dir is None:
            source_dir = "./CSV/"

        self.set_source_dir(source_dir)

        if source_file is None:
            source_file = "FirstNames-Popularity-fr.csv"

        self.set_source_file(source_file)

        data = RandomNamesGenerator.read_file(source_dir, source_file)

        if len(column_names) > 0:
            data.rename(columns=column_names, inplace=True)
        
        self.set_data(data)
        # print(self.get_data())

    ### GETTERS and SETTERS ###

    def get_column_names(self) -> list():
        return copy.deepcopy(self._column_names)

    def set_column_names(self, column_names=list()) -> None:
        self._column_names = column_names

    def get_num_rows(self) -> int:
        return copy.copy(self._num_rows)

    def set_num_rows(self, num_rows=int) -> None:
        self._num_rows = num_rows

    def get_source_dir(self) -> str:
        return copy.copy(self._source_dir)

    def set_source_dir(self, source_dir=str) -> None:
        self._source_dir = source_dir

    def get_source_file(self) -> str:
        return copy.copy(self._source_file)

    def set_source_file(self, source_file=str) -> None:
        self._source_file = source_file

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
        new_frame = RandomNamesGenerator.drop_data_column(
            data_frame, column)
        self.set_data(new_frame)
        return new_frame

    def print_data_frame(self) -> None:
        print(self.get_data())

    ### CLASS METHODES ###

    @classmethod
    def build_path(cls, dir_path=str, file_name=str) -> str:
        return dir_path + file_name

    @classmethod
    def read_file(cls, source_dir=str, source_file=str) -> DataFrame:
        path = RandomNamesGenerator.build_path(source_dir, source_file)
        return pandas.read_csv(filepath_or_buffer=path)

    @classmethod
    def return_percentage(cls, data=DataFrame, sort_index=str, percentage=100, ascend=False) -> DataFrame:
        if ascend is None:
            ascend = False # Default rank order to descending
        data.sort_values(by=sort_index, ascending=ascend,
                         kind="mergesort", inplace=True)

        dec_percent = Decimal(1) # Default the percentage of names to 100
        if percentage < 100:
            dec_percent = Decimal(f"0." + f"{percentage}") # Set to a Decimal percentage

        total_names = len(data)
        num_names = int((total_names * dec_percent).to_integral()) # calculate num rows from top to return
        new_data = copy.copy(data.head(num_names))

        return new_data

    @classmethod
    def drop_data_column(cls, data_table=DataFrame, drop_column=list()) -> DataFrame:
        return data_table.drop(drop_column, axis=1)

    @classmethod
    def sort_data_table(cls, data_table=DataFrame, sort_columns=list(), ascend:bool=False) -> DataFrame:
        return data_table.sort_values(by=sort_columns, ascending=ascend, kind="mergesort")

    @classmethod
    def truncate_data_table(cls, data_table=DataFrame, num_rows=int) -> DataFrame:
        return data_table.head(num_rows)

    @classmethod
    def randomize_rows(cls, data_table=DataFrame, num_rows=int) -> DataFrame:
        return data_table.sample(num_rows)

    @classmethod
    def prepare_data_frame(cls, names_gen:RandomNamesGenerator, columns_order:list, drop_columns:list=None, final_order:list=None, sort_columns:list=None, percentage:int=100, ascending:bool=False) -> DataFrame:
        # data = cls.read_file(names_gen.get_source_dir(), names_gen.get_source_file())

        data = cls.return_percentage(names_gen.get_data(), sort_columns, percentage, ascending)
        
        if len(names_gen.get_column_names()) > 0:
            data.rename(columns=names_gen.get_column_names(), inplace=True)

        data = cls.sort_data_table(data, sort_columns, ascending)
        data = cls.truncate_data_table(data, names_gen.get_num_rows())
        data = cls.sort_data_table(data, final_order, ascending)

        if drop_columns is not None:
            data = cls.drop_data_column(data, drop_columns)

        data = cls.randomize_rows(data, names_gen.get_num_rows())
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
