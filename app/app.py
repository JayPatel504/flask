from flask import Flask, redirect, url_for, request, render_template, flash
from ..calc.calculate import Calculate

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route('/', methods = ['GET'])
def home():
    return render_template('index.html')

@app.route('/cal', methods = ['GET','POST'])
def calc():
    if request.method == 'GET':
        return render_template('calculator.html', left='1', middle='+', right='1', res='2')
    
    left, middle, right = request.form['left'], request.form['middle'], request.form['right']
    res = ''
    if not left or not right:
        flash("Missing Value")
        return render_template('calculator.html', left='1', middle='+', right='1', res='2')
    
    if middle == '+':
        res = str(float(left) + float(right))
    elif middle == '-':
        res = str(float(left) - float(right))
    else:
        flash("Not Supported OP")
        return render_template('calculator.html',left='1', middle='+', right='1', res='2')

    with open('history.csv', 'a+') as writer:
        line = f'{left},{middle},{right},{res}\n'
        writer.write(line) 
    with open('history.csv', 'r') as reader:
        csv = reader.read().split('\n')
    new_csv=[]
    for line in csv:
        new_csv.append(line.split(','))
    return render_template('calculator.html', left=left, middle=middle, right=right, res=res)

@app.route('/results', methods = ['GET'])
def results():
    return render_template('table.html', title='Bootstrap Table', df=Calculate.getDF())

if __name__ == '__main__':
   app.run(debug = True,port=7894)