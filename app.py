#Copyright Bail 2025
#HistoryExercise 历史选择题练习场 v1.0_1
#2025.6.15

from flask import Flask, render_template
import libproblem

app = Flask(__name__)
app.register_blueprint(libproblem.app)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=8081)
