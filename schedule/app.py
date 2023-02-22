from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
@app.route("/health")
def main():
    return render_template('main.html')
    # return "<p>Hello, World!</p>"


if __name__ == '__main__':
    app.run(debug=True)