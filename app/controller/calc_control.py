'''script for calc'''
#pylint: disable=E0401,E1136,E0213,E1135,C0103,W0702
from app.controller.control import ControllerBase
from app.calc.calculate import Calculate
from flask import request, render_template, flash

class calcControl(ControllerBase):
    '''Class for flask calc'''
    @staticmethod
    def get():
        '''returns page'''
        return render_template('calculator.html',left='1',right='1')
    @staticmethod
    def post():
        '''does calc'''
        left, middle, right = request.form['left'], request.form['middle'], request.form['right']
        try:
            _,_=float(left),float(right)
        except:
            flash("Invalid Value")
            return render_template('calculator.html',left='1',right='1')

        if not left or not right:
            flash("Missing Value")
            return render_template('calculator.html',left='1',right='1')

        flash("Result Generated")
        getattr(Calculate(), middle)((left,right))
        Calculate.writeHistoryToCSV()
        return render_template('calculator.html',left='1',right='1')
