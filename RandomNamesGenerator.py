from ListBuilder import ListBuilder
from decimal import Decimal
import copy

import pandas
from pandas import DataFrame


class RandomNamesGenerator(ListBuilder):

    ######## Constructor ########

    def __init__(self, source_dir=str, source_file=str):
        super().__init__(source_dir, source_file)

        self.set_num_rows(0)

    ### GETTERS and SETTERS ###

    def set_num_rows(self, num_rows=int) -> None:
        self._num_rows = num_rows

    ### INSTANCE METHODES ###

    def order_by_popularity(self, ascend=bool) -> DataFrame:
        data_frame = self.get_data()
        return data_frame.sort_values(by="Popularity", ascending=ascend, kind="mergesort")

    ### CLASS METHODES ###

    @classmethod
    def return_percentage(cls, data=DataFrame, percentage=100, ascend=False) -> DataFrame:
        if ascend is None:
            ascend = False # Default rank order to descending

        sort_index = data.columns[len(data.columns) - 1]
        
        data.sort_values(by=sort_index, ascending=ascend,
                         kind="mergesort", inplace=True)

        num_names = cls.calculate_percentage_num_rows(data, percentage)

        new_data = copy.copy(data.head(num_names))

        return new_data

    @classmethod
    def calculate_percentage_num_rows(cls, data=DataFrame, percentage=100.00) -> int:
        dec_percent = Decimal(1)  # Default the percentage of names to 100
        if percentage < 100 and percentage >= 10:
            # Set to a Decimal percentage
            dec_percent = Decimal(f"0." + f"{percentage}")
        if percentage > 0 and percentage <= 10:
            dec_percent = Decimal(f"0{percentage}")
        
        total_names = len(data)
        # calculate num rows from top to return
        return int((total_names * dec_percent).to_integral())

    @classmethod
    def prepare_data_frame(cls, names_gen: ListBuilder, column_names:list, drop_columns: list = None, final_order: list = None,
                            sort_columns:list=None, num_rows:int=20, percentage: int = 100, ascending: bool = False) -> DataFrame:
        
        percentage_rows = cls.calculate_percentage_num_rows(names_gen.get_data(), percentage)

        if len(column_names) > 0:
            names_gen.set_column_names(column_names)
        
        if len(column_names) > 0:
            names_gen.get_data().rename(columns=column_names, inplace=True)
        
        if num_rows is not None:
            names_gen.set_num_rows(num_rows)
        
        if percentage_rows < num_rows:
            num_rows = percentage_rows

        data = cls.return_percentage(names_gen.get_data(), percentage, ascending)
        
        if len(names_gen.get_column_names()) > 0:
            data.rename(columns=names_gen.get_column_names(), inplace=True)

        data = cls.sort_data_table(data, sort_columns, ascending)
        data = cls.truncate_data_table(data, num_rows)
        data = cls.sort_data_table(data, final_order, ascending)

        if drop_columns is not None:
            data = cls.drop_data_column(data, drop_columns)

        data = cls.randomize_rows(data, num_rows)
        return data
