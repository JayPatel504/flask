""" This is the increment function"""
#pylint: disable=E0401,E0213,E1101,R0903,R1732,C0103,C0301
from ..operation.addition import Addition
from ..operation.subtraction import Subtraction
from ..operation.multiplication import Multiplication
from ..operation.division import Division
from ..csv.readCSV import Reading
from ..csv.writeCSV import Writing

class Calculator:
    """ This is the Calculator class"""
    history = []
    df = Reading.read()
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
    def writeHistoryToCSV():
        """read from history, write to CSV"""
        last_result=Calculator.get_last_calculation()
        calc_list=list(last_result.values)
        calc_list.append(last_result.__class__.__name__)
        calc_list.append(last_result.get_result())
        print("129-jrfnek")
        print(calc_list)
        Calculator.df.loc[len(Calculator.df.index)] = calc_list

        Writing.writeL(Calculator.df)
        return True
    @staticmethod
    def getdf():
        '''get df'''
        return Calculator.df
