'''Read CSV and performs operation'''
#pylint: disable=E0401,E1136,E0213,E1135,C0103
import pandas as pd
import os

class Reading:
    '''Reading Class'''
    def read():
        '''Read CSV and find what operation is needed'''
        f_path = os.path.join(os.path.abspath(__file__),'..','..',"data/history.csv")
        return pd.read_csv(f_path)
