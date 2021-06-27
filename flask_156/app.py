from flask import Flask
from werkzeug.middleware.proxy_fix import ProxyFix

from country import api

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

api.init_app(app)
app.run(debug=True)


















# api = Api(app, version='1.0', title='Central156 API',
#     description='Api para o TCC Statistics 156',
# )


# ns = api.namespace('tasks', description='tasks op')

# todo = api.model('task', {
#      'id': fields.Integer(readonly=True, description='The task unique identifier'),
#     'name': fields.String(required=True, description='The task details'),
#     "totalCases": fields.Integer(),
#     "totalDeaths": fields.Integer()
# })

# DAO = appService
# DAO.create({'task': 'Build an API'})
# DAO.create({'task': '?????'})
# DAO.create({'task': 'profit!'})


# @ns.route('/')
# class TodoList(Resource):
#     '''Shows a list of all todos, and lets you POST to add new tasks'''
#     @ns.doc('list_todos')
#     @ns.marshal_list_with(todo)
#     def get(self):
#         '''List all tasks'''
#         return DAO.todos

#     @ns.doc('create_todo')
#     @ns.expect(todo)
#     @ns.marshal_with(todo, code=201)
#     def post(self):
#         '''Create a new task'''
#         return DAO.create(api.payload), 201


# @ns.route('/<int:id>')
# @ns.response(404, 'Todo not found')
# @ns.param('id', 'The task identifier')
# class Todo(Resource):
#     '''Show a single todo item and lets you delete them'''
#     @ns.doc('get_todo')
#     @ns.marshal_with(todo)
#     def get(self, id):
#         '''Fetch a given resource'''
#         return DAO.get(id)

#     @ns.doc('delete_todo')
#     @ns.response(204, 'Todo deleted')
#     def delete(self, id):
#         '''Delete a task given its identifier'''
#         DAO.delete(id)
#         return '', 204

#     @ns.expect(todo)
#     @ns.marshal_with(todo)
#     def put(self, id):
#         '''Update a task given its identifier'''
#         return DAO.update(id, api.payload)


# if __name__ == '__main__':
#     app.run(debug=True)