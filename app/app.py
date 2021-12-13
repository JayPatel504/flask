'''Flask Program'''
from app.controller.calc_control import calcControl
from app.controller.result import results_fac
from flask import Flask, request, render_template

app = Flask(__name__,static_url_path='/static')
app.secret_key = "super secret key"

@app.route('/', methods = ['GET'])
def home():
    '''home route'''
    return render_template('index.html')

@app.route('/cal', methods = ['GET','POST'])
def calc():
    '''calc route'''
    if request.method == 'GET':
        return calcControl.get()
    return calcControl.post()

@app.route('/results', methods = ['GET'])
def results():
    '''table route'''
    return results_fac.table_page()

@app.route('/four', methods = ['GET'])
def four():
    '''mystery'''
    return render_template('four.html')

if __name__ == '__main__':
    app.run()
