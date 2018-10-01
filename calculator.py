from flask import Flask,render_template, request, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/')
def cal():
        return render_template('calculator.html')



@app.route('/add/')
def add():
	return render_template('add.html')


@app.route('/add_result')
def add_result():
		num1 = request.args.get('Num1')
		num2 = request.args.get('Num2')
		ans = int(num1) + int(num2)
		return jsonify(result = ans)

    
@app.route('/subtract/')
def subtract():
        return render_template('subtract.html')

@app.route('/subtract_result')
def subtract_result():
		num1 = request.args.get('Num1')
		num2 = request.args.get('Num2')
		ans = int(num1) - int(num2)
		return jsonify(result = ans)

@app.route('/divide/')
def divide():
        return render_template('divide.html')

@app.route('/divide_result')
def divide_result():
		num1 = request.args.get('Num1')
		num2 = request.args.get('Num2')
		ans= int(num1) / int(num2)
		return jsonify(result = ans)

@app.route('/multiply/')
def multiply():
        return render_template('multiply.html')

@app.route('/multiply_result')
def multiply_result():
		num1 = request.args.get('Num1')
		num2 = request.args.get('Num2')
		ans= int(num1) * int(num2)
		return jsonify(result = ans)


if __name__ == '__main__':
    app.run(debug=True)
