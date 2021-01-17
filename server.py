from flask import Flask, render_template, request, make_response, jsonify
from FindWord import findWord
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/find-word/')
# def find_word():
#   print ('I got clicked!')

#   return findWord('WARZN')


@app.route('/', methods=['POST'])
def find_word():
    inputWord = request.get_json()
    result = findWord(inputWord)
    res = make_response(jsonify(result), 200)

    return res

if __name__ == '__main__':
    app.run(debug=True)
