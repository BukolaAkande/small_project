from flask import Flask, render_template, request
import os
app = Flask(__name__)


@app.route('/')
def index():
    return '''
                <h1>Hello Welocme to website</h1>
                <button onclick="window.location.href = '/home'" > click here to get started</button>
            '''

@app.route('/home')
def index2():
    return render_template('index.html')

@app.route('/button_clicked', methods=["POST"])
def button_clicked():
    location = request.form.get("userLocation")
    username = request.form.get("username")
    print(f'The user location is {location} and username is {username}' )
    return "Button clicked!"

if __name__ == '__main__':
        port = int(os.environ.get('PORT', 5000))
        app.run(debug=True, host='0.0.0.0', port=port)