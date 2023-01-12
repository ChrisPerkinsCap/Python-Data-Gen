from faker import Faker

from pandas import DataFrame

from faker.providers import BaseProvider

import RandomNamesGenerator

fake = Faker()

class FakerFirstNamesProvider(BaseProvider):

    def __init__(self, generator: Any) -> None:
        super().__init__(generator)
        self._source_dir = "./CSV/"
        self._source_file = "FirstNames-fr.csv"
        self._target_file = "FirstNames-Popularity-fr.csv"
        self._drop_columns = ["NameCount", "Rand"]
        self._sort_columns = ["NameCount"]
        self._final_sort = ["name", "sex", "NameCount", "Rand"]
        self._columns_order = ["NameCount", "sex", "name", "Rand"]
        self._num_rows = 172



    def genderedFirstNames(self, columns_order=list(), drop_columns=list(), final_sort=list(),
                            num_rows=int, sort_columns=list(), source_dir=str, source_file=str) -> DataFrame:


        RG = RandomNamesGenerator(columns_order, drop_columns, final_sort, num_rows,
                                         sort_columns, source_dir, source_file)
        return RG.


fake.add_provider(FakerFirstNamesProvider)