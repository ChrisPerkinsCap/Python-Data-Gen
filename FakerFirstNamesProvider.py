from faker import Faker

from pandas import DataFrame

from faker.providers import BaseProvider

import GenerateRandomFirstNamesCSV

fake = Faker()

class FakerFirstNamesProvider(BaseProvider):

    

    def genderedFirstNames(self, columns_order=list(), drop_columns=list(), final_sort=list(),
                            num_rows=int, sort_columns=list(), source_dir=str, source_file=str, target_file=str) -> DataFrame:
        source_dir = "./CSV/"
        source_file = "FirstNames-fr.csv"
        target_file = "FirstNames-fr-Popularité.csv"
        drop_columns = ["NameCount", "Rand"]
        sort_columns = ["NameCount"]
        final_sort = ["name", "sex", "NameCount", "Rand"]
        columns_order = ["NameCount", "sex", "name", "Rand"]
        num_rows = 172

        RG = GenerateRandomFirstNamesCSV(columns_order, drop_columns, final_sort, num_rows,
                                         sort_columns, source_dir, source_file)
        return RG
