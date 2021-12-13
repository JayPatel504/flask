"""Testing the Calculator"""
#pylint: disable=E0401,E1136,E0213,E1135,C0103,C0301,C0123
import pathlib
import os
from app.calc.history.calculator import Calculator
from app.calc.calculate import Calculate
import pandas as pd
import pytest

@pytest.fixture(name="clear_history",autouse=True)
def fixture_clear_history():
    '''clear history function'''
    Calculator.add_numbers((1,2))
    yield
    Calculator.clear_history()

def test_get_result_of_first_calculation_added_to_history():
    '''test to get result of first calc'''
    assert Calculator.get_result_of_first_calculation_added_to_history() == 3.0

def test_clear_history():
    '''test to clear history'''
    assert Calculator.clear_history()
    assert Calculator.history_count() == 0

def test_get_last_calculation():
    '''test to get last calc'''
    assert Calculator.get_last_calculation().get_result() == 3.0

def test_get_first_calculation():
    '''test to get first calc'''
    assert Calculator.get_first_calculation().get_result() == 3.0

def test_history_count():
    '''test to count history'''
    assert Calculator.history_count() == 1

def test_add_calculation():
    '''test for add calc to list'''
    assert Calculator.history_count() == 1

def test_get_last_result_value():
    '''test to get result of last calc'''
    assert Calculate.get_last_result_value() == 3.0

def test_get_calculation_object():
    '''test to get object'''
    assert Calculator.get_calculation_object(0).get_result() == 3.0

def test_addition():
    """Testing the Add function of the calculator"""
    Calculate.addition((1,2,3,4))
    assert Calculator.get_result_of_last_calculation_added_to_history() == 10.0

def test_subtraction():
    """Testing the subtract method of the calculator"""
    Calculate.subtraction((10,7))
    assert Calculator.get_result_of_last_calculation_added_to_history() == -17.0

def test_multiplication():
    """ tests multiplication of two numbers"""
    Calculate.multiplication((2,2,2))
    assert Calculator.get_result_of_last_calculation_added_to_history() == 8.0

def test_division():
    """ tests division of two numbers"""
    Calculate.division((2,2))
    assert Calculator.get_result_of_last_calculation_added_to_history() == 1.0
    Calculate.division((2,0))
    assert Calculator.get_result_of_last_calculation_added_to_history() == "Can't divide by zero"

def test_getHistory():
    '''Tests getting history array'''
    assert Calculate.getHistory() == Calculator.history

def test_DF():
    '''tests getting df from csv'''
    assert type(Calculate.getDF()) == type(pd.DataFrame(columns = ["Value 1","Value2","Operation","Result"]))

def test_writeHistoryToCSV():
    '''tests writing to csv'''
    Calculate.writeHistoryToCSV()
    x = pathlib.Path(os.path.join(os.path.dirname(os.path.abspath(__file__)),'..',"data","history.csv"))
    assert x.is_file()
