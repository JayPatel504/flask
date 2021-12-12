from controller.control import ControllerBase
from flask import Flask, redirect, url_for, request, render_template, flash
from calc.calculate import Calculate
class calcControl(ControllerBase):
    @staticmethod
    def get():
        return render_template('calculator.html',left='1',right='1')
    @staticmethod
    def post():
        obj=Calculate
        left, middle, right = request.form['left'], request.form['middle'], request.form['right']
        
        if not left or not right:
            flash("Missing Value")
            return render_template('calculator.html',left='1',right='1')
        try:
                
            print("here123")
            print(middle)
            getattr(obj, middle)(left,right)
            print("here")
                
            # Calculate.writeHistoryToCSV()
        except:
            flash("Not Supported OP")
            # return render_template('calculator.html')

        return render_template('calculator.html',left='1',right='1')