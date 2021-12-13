'''Script for displaying table page'''
#pylint: disable=E0401,E1136,E0213,E1135,C0103,R0903
from app.controller.control import ControllerBase
from app.calc.calculate import Calculate
from flask import render_template

class results_fac(ControllerBase):
    '''displays table'''
    @staticmethod
    def table_page():
        '''displays table from df'''
        return render_template('table.html', title='History Table', df=Calculate.getDF())
