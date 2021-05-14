from flask import Flask, render_template, request


app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/calculadora', methods=['POST'])
def send(total=sum):
    if request.method == 'POST':
        
        num1 = request.form['num1']
        num2 = request.form['num2']
        operacion = request.form['operacion']

        if operacion == 'suma':
            total = float(num1) + float(num2)
            return render_template('index.html', total=total)

        elif operacion == 'resta':
            total = float(num1) - float(num2)
            return render_template('index.html', total=total)

        elif operacion == 'multiplicacion':
            total = float(num1) * float(num2)
            return render_template('index.html', total=total)

        elif operacion == 'division':
            try:
                total = float(num1) / float(num2)
                return render_template('index.html', total=total)

            except ZeroDivisionError as total:
                return render_template('index.html', total=total)
        else:
            return render_template('index.html')


if __name__ == ' __main__':
    app.debug = True
    app.run()

