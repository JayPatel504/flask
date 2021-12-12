from controller.control import ControllerBase
from flask import render_template
from calc.calculate import Calculate

class results_fac(ControllerBase):
    @staticmethod
    def table_page():
        return render_template('table.html', title='History Table', df=Calculate.getDF())