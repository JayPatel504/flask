from flask import Flask, redirect, url_for, request, render_template, flash

from controller.calc_control import calcControl 
from controller.result import results_fac

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html')

@app.route('/cal', methods = ['GET','POST'])
def calc():
    if request.method == 'GET':
        return calcControl.get()
    else:
        return calcControl.post()


@app.route('/results', methods = ['GET'])
def results():
    return results_fac.table_page()
    # return render_template('table.html', title='Bootstrap Table', df=Calculate.getDF())

if __name__ == '__main__':
   app.run()