from flask import Flask, redirect, request, url_for, render_template
import os
import openai

api_key = os.environ['OPENAI_API_KEY']

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search', methods=['POST'])
def submit():
    userInput = request.form['msg']
    return redirect(url_for('result', message=userInput))

@app.route('/result/<message>')
def result(message):
    completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": "review my message and provide feedback to improve English skills, tell my mistake and also tell 3 new vocabulary words with their meaning related to context of message, feedback should not exceed limit of 900 characters and do not greet throughout the message " + message}])
    aiMsg = completion.choices[0].message.content
    return render_template('result.html', msg=message, aiMsg=aiMsg)


if __name__ == '__main__':
    app.run()



