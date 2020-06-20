from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/main.html')
def main_page():
     return render_template('main.html')

@app.route('/about.html')
def about_page():
     return render_template('about.html')

@app.route('/content.html')
def content_page():
     return render_template('content.html')

@app.route('/tests.html')
def test_page():
     return render_template('tests.html')


# Добавим возможность "запуска файла"
if __name__ == "__main__":
    app.run(debug = True)