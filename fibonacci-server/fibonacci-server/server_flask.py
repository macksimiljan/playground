from flask import Flask

import fibonacci

app = Flask(__name__)


@app.route('/fib/<int:n>')
def fib(n: int):
    number = fibonacci.fib(n)
    return {'n': n, 'number': number}


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=False, use_reloader=False)
