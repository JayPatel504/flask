""" This is the increment function"""

from operation.addition import Addition
from operation.subtraction import Subtraction
from operation.multiplication import Multiplication
from operation.division import Division
from ...csv.readCSV import Reading
from ...csv.writeCSV import Writing
import pandas as pd
import numpy as np

class Calculator:
    """ This is the Calculator class"""
    history = []
    @staticmethod
    def get_result_of_first_calculation_added_to_history():
        '''result of first entry'''
        return Calculator.history[0].get_result()
    @staticmethod
    def clear_history():
        '''clear list'''
        Calculator.history.clear()
        return True
    @staticmethod
    def get_last_calculation():
        '''get last calc'''
        return Calculator.history[-1]
    @staticmethod
    def get_first_calculation():
        '''get first calc'''
        return Calculator.history[0]
    @staticmethod
    def history_count():
        '''len(list)'''
        return len(Calculator.history)
    @staticmethod
    def add_calculation(calculation):
        '''add calculation object to list'''
        Calculator.history.append(calculation)
        return True
    @staticmethod
    def get_result_of_last_calculation_added_to_history():
        '''get last result'''
        return Calculator.get_last_calculation().get_result()
    @staticmethod
    def get_calculation_object(num):
        '''get specified object'''
        return Calculator.history[num]
    @staticmethod
    def add_numbers(tuple_values: tuple):
        """ add numbers to result"""
        Calculator.add_calculation(Addition.create(tuple_values))
        return True
    @staticmethod
    def subtract_numbers(tuple_values: tuple):
        """ subtract numbers from result"""
        Calculator.add_calculation(Subtraction.create(tuple_values))
        return True
    @staticmethod
    def multiply_numbers(tuple_values: tuple):
        """ multiply numbers and store the result"""
        Calculator.add_calculation(Multiplication.create(tuple_values))
        return True
    @staticmethod
    def divide_numbers(tuple_values: tuple):
        """ divide numbers and store the result"""
        Calculator.add_calculation(Division.create(tuple_values))
        return True
    @staticmethod
    def readHistoryFromCSV():
        """read entries from CSV, store in history"""
        df = Reading.read().to_numpy()
        for x in df:            
            if 'add' in x[2]:
                Calculator.add_numbers((x[0],x[1]))
            elif 'sub' in x[2]:
                Calculator.subtract_numbers((x[0],x[1]))
            elif 'multi' in x[2]:
                Calculator.multiply_numbers((x[0],x[1]))
            else:
                Calculator.divide_numbers((x[0],x[1]))             
        return True
    @staticmethod
    def writeHistoryToCSV():
        """read from history, write to CSV"""
        q=[]
        for x in Calculator.history:
            t=list(x.values)
            t.append(x.__class__.__name__)
            t.append(x.get_result())
            q.append(t)
        ss= np.array(q)
        Writing.writeL(pd.DataFrame(ss,columns=['Value 1', 'Value 2', 'Operation','Result']))
        return True
