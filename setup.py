from flask import Flask , render_template , request 
import whisper
import os

app = Flask(__name__)

@app.route('/')
def init_html():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def user():
    if request.method == 'POST':
        file = request.files['file']
        file.save(file.filename)
        model = whisper.load_model('base')
        result = model.transcribe(file.filename,fp16=False)
        if os.path.exists(file.filename):
            os.remove(file.filename)
        return result['text']

if __name__ == '__main__':
    app.run(debug=True,port=8080)
    
