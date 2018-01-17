from flask import Flask, render_template


app = Flask(__name__)

# user = 'az2498'

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/az2498', methods=['GET'])
def about_me():
    return render_template('aboutme.html')


if __name__ == '__main__':
    app.run()
