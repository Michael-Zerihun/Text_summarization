from flask import Flask, render_template, request
from transformers import pipeline

summarizer = pipeline('summarization')

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/summarize', methods=['POST'])
def summarize():
    summary = summarizer(request.form.get('text'), max_length=100, min_length=100, do_sample=False)
    return render_template('index.html', summary=summary[0]['summary_text'], text=request.form.get('text') )

# @app.route('/summarize',methods=['POST'])
# def summarize():
#     summary = summarizer(request.form.get('text'), max_length=100, min_length=100, do_sample=True)
#     return summary[0]['summary_text']
if __name__ == '__main__':
    app.run(debug=True)