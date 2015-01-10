from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good tutorial',
        'done': False
    }
]

@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error':'Not Found'}), 404)

@app.route('/todo/api/v1/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks':tasks})

@app.route('/todo/api/v1/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/')
def index():
    return "HELLOW CREWEL WORLD"

if __name__ == '__main__':
    app.run(debug=True)
