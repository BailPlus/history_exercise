#HistoryExercise:libproblem 题目处理库

from flask import Blueprint, request
import sqlite3

app = Blueprint('libproblem', __name__, url_prefix='/problems')
def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d
db = sqlite3.connect('problems.db', check_same_thread=False)
db.row_factory = dict_factory

@app.get('/<int:problem_id>')
def get_problem_by_id(problem_id):
    with db:
        cursor = db.cursor()
        cursor.execute('SELECT * FROM problems WHERE id = ?', (problem_id,))
        problems = cursor.fetchall()
        if not problems:
            return {
                'success': False,
                'error': '无此题号'
            }, 404
        return {
            'success': True,
            'problems': problems
        }

@app.get('/random')
def random_problem():
    num = int(request.args.get('num','1'))
    if num > 100: 
        return {
            'success': False,
            'error': '太多了，不超过100道题哦'
        }
    elif num < 1:
        return {
            'success': False,
            'error': f'你给我造{num}个题目去'
        }
    with db:
        problems = db.cursor()\
            .execute(
                'SELECT * FROM problems ORDER BY RANDOM() LIMIT ?',
                (num,)
            )\
            .fetchall()
    return {
        'success': True,
        'problems': problems
    }

@app.get('/search')
def search_problem():
    keyword = request.args.get('q','')
    if not keyword.strip():
        return {
            'success': False,
            'error': '请输入查询关键词'
        }
    with db:
        problems = db.cursor()\
            .execute(
                'SELECT * FROM problems WHERE problem LIKE ?',
                (f'%{keyword}%',)
            )\
            .fetchall()
    return {
        'success': True,
        'problems': problems
    }
