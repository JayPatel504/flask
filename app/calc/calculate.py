""" This is the increment function"""
#pylint: disable=E0401,E1136,E0213,E1135,C0103,E0211
from .history.calculator import Calculator

#the calculator class just contains the methods to calculate
class Calculate:
    """ This is the Calculate class"""
    #the calculator class just calls methods on Calculator class
    @staticmethod
    def get_last_result_value():
        """ This is the gets the result of the calculation"""
        # I made this method so that I don't have more than one action per function
        return Calculator.get_result_of_last_calculation_added_to_history()
    @staticmethod
    #tuple allows me to pass in as many values as a I want
    def addition(tuple_values: tuple):
        """ adds list of numbers"""
        Calculator.add_numbers(tuple_values)
        return True
    @staticmethod
    def subtraction(tuple_values: tuple):
        """ subtract a list of numbers from result"""
        Calculator.subtract_numbers(tuple_values)
        return True
    @staticmethod
    def multiplication(tuple_values: tuple):
        """ multiplication number from result"""
        Calculator.multiply_numbers(tuple_values)
        return True
    @staticmethod
    def division(tuple_values: tuple):
        """ divide number from result"""
        Calculator.divide_numbers(tuple_values)
        return True
    @staticmethod
    def getHistory():
        """ Get history """
        return Calculator.history
    def getDF():
        """Read from CSV"""
        return Calculator.getdf()
    @staticmethod
    def writeHistoryToCSV():
        """Write to CSV """
        return Calculator.writeHistoryToCSV()
