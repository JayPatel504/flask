import pandas as pd

class Read:
    @staticmethod
    def DataFrameFromCSVFile(filename):
        return pd.read_csv(filename)