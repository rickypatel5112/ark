from flask import Flask, render_template, request, send_file
from flask_cors import CORS

from commands import handle_audio_input, handle_text_input

app = Flask(__name__)
CORS(app)


@app.route('/')
def home():
   return render_template('index.html')

@app.route('/about')
def about():
   return render_template('about.html')

@app.route('/features')
def features():
   return render_template('features.html')

@app.route('/commands')
def commands():
   return render_template('commands.html')

@app.route('/text_input', methods=['POST'])
def text_input():
   query = request.form['text-input']
   return handle_text_input(query)


@app.route('/audio_input')
def hello_name():
    query = handle_audio_input()
    return query

@app.route('/audio')
def send_audio_file():
  return send_file("static/audiofile.wav", "audio/wav")

if __name__ == '__main__':
   app.run(debug=True)
