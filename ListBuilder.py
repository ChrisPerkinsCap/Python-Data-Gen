from __future__ import annotations
import copy
from datetime import datetime
import os
from os.path import exists
from os import mkdir


import pandas
from pandas import DataFrame


class ListBuilder:

    ######## Constructor ########

    def __init__(self, source_dir=str, source_file=str):

        self.set_column_names(list())

        if source_dir is None:
            source_dir = "./CSV/"

        self.set_source_dir(source_dir)

        if source_file is None:
            source_file = "FirstNames-Popularity-fr.csv"

        self.set_source_file(source_file)

        data = ListBuilder.read_file(source_dir, source_file)

        self.set_data(data)
        # print(self.get_data())

        self.set_cwd_path()

    ### GETTERS and SETTERS ###

    def get_column_names(self) -> list():
        return copy.deepcopy(self._column_names)

    def set_column_names(self, column_names=list()) -> None:
        self._column_names = column_names

    def get_num_rows(self) -> int:
        return copy.copy(self._num_rows)

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
    
    def set_cwd_path(self) -> str:
        self._cwd_path = os.getcwd()

    ### INSTANCE METHODES ###

    def remove_column(self, column_name=str) -> DataFrame:
        data_frame = self.get_data()
        column = [column_name]
        new_frame = ListBuilder.drop_data_column(
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
        path = ListBuilder.build_path(source_dir, source_file)
        pd = pandas.read_csv(filepath_or_buffer=path)
        return pd

    @classmethod
    def drop_data_column(cls, data_table=DataFrame, drop_column=list()) -> DataFrame:
        return data_table.drop(drop_column, axis=1)

    @classmethod
    def sort_data_table(cls, data_table=DataFrame, sort_columns=list(), ascend: bool = False) -> DataFrame:
        return data_table.sort_values(by=sort_columns, ascending=ascend, kind="mergesort")

    @classmethod
    def truncate_data_table(cls, data_table=DataFrame, num_rows=int) -> DataFrame:
        return data_table.head(num_rows)

    @classmethod
    def randomize_rows(cls, data_table=DataFrame, num_rows=int) -> DataFrame:
        return data_table.sample(num_rows)

    @classmethod
    def create_directory(cls, directory=str) -> bool:
        success = False
        if len(directory) > 0 and not exists(directory):
            success = mkdir(directory)
        return success

    @classmethod
    def write_to_csv(cls, data=DataFrame, target_directory=str, target_file=str) -> bool:
        if target_file is None:
            dt = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
            target_file = f"FirstNames-Popularity-fr{dt}.csv"

        if target_directory is None:
            target_directory = "./CSV/"

        cls.create_directory(target_directory)

        file_path = target_directory + target_file + ".csv"
        data
        data.to_csv(file_path, index=False)
        return exists(file_path)

    @classmethod
    def write_to_xlsx(cls, data=DataFrame, target_directory=str, target_file=str) -> bool:
        if target_file is None:
            dt = datetime.now().strftime("%d-%m-%Y_%H-%M-%S")
            target_file = f"FirstNames-Popularity-fr{dt}.csv"

        if target_directory is None:
            target_directory = ["./CSV/"]

        cls.create_directory(target_directory)

        file_path = target_directory + target_file + ".xlsx"
        data.to_excel(file_path, index=False)
        return exists(file_path)
