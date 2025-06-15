#HistoryExercise:libproblem 题目处理库

from flask import Blueprint
import sqlite3

app = Blueprint('libproblem', __name__, url_prefix='/problems')
db = sqlite3.connect('problems.db', check_same_thread=False)

@app.route('/<int:problem_id>')
def get_problem_by_id(problem_id):
    with db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM problems WHERE id = ?', (problem_id,))
        problem = cursor.fetchone()
        if not problem:
            return {
                'success': False,
                'info': '无此题号'
            }, 404
        return {
            'success': True,
            'id': problem[0],
            'description': problem[1],
            'A': problem[2],
            'B': problem[3],
            'C': problem[4],
            'D': problem[5],
            'answer': problem[6],
        }

@app.route('/random')
def random_problem():