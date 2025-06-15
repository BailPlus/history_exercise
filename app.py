#Copyright Bail 2025
#HistoryExercise 历史选择题练习场 v1.0_1
#2025.6.15

from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

