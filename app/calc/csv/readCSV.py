'''Read CSV and performs operation'''
#pylint: disable=E0401,E1136,E0213,E1135,C0103,E0211,R0903,W0702,C0301
import os
import pandas as pd

class Reading:
    '''Reading Class'''
    def read():
        '''Read CSV and find what operation is needed'''
        f_path = os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','..',"data","history.csv")
        try:
            return pd.read_csv(f_path)
        except:
            return pd.DataFrame(columns = ["Value1","Value2","Operation","Result"])
