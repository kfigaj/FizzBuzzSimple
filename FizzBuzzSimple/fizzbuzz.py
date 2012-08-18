from flask import Flask, request, render_template
from helper import fizzbuzz

app = Flask(__name__)
app.config.from_object('settings')


@app.route('/', methods=['POST', 'GET'])
def main():
    if request.method == 'POST':
        rounds = request.form['rounds']
        results = fizzbuzz(rounds)
        return render_template('fizzbuzz.html', results=results)

    return render_template('fizzbuzz.html')

if __name__ == '__main__':
    app.run()
