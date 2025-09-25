from flask import Flask, render_template
import webbrowser
import threading

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

def open_browser():
    webbrowser.open("http://127.0.0.1:9900/")

if __name__ == '__main__':
    # รันเว็บเซิร์ฟเวอร์บน http://127.0.0.1:9900
    threading.Timer(1.0, open_browser).start()
    app.run(debug=True, port=9900)

