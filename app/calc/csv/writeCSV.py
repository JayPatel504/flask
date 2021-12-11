'''Writing results to log file'''
#pylint: disable=E0401,E0213,E1101,R0903,R1732,C0103,C0301
import pandas as pd
import os
import io


class Writing:
    '''Writing Class'''
    def writeL(df):
        '''Writing out'''
        f_path = os.path.join(os.path.abspath(__file__),'..','..',"data/history.csv")
        return df.to_csv(f_path, index=True, header=True)
